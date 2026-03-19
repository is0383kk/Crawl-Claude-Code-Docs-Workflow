> ## Documentation Index
> Fetch the complete documentation index at: https://docs.openclaw.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Azure

# OpenClaw on Azure Linux VM

This guide sets up an Azure Linux VM, applies Network Security Group (NSG) hardening, configures Azure Bastion (managed Azure SSH entry point), and installs OpenClaw.

## What you’ll do

* Deploy Azure compute and network resources with Azure Resource Manager (ARM) templates
* Apply Azure Network Security Group (NSG) rules so VM SSH is allowed only from Azure Bastion
* Use Azure Bastion for SSH access
* Install OpenClaw with the installer script
* Verify the Gateway

## Before you start

You’ll need:

* An Azure subscription with permission to create compute and network resources
* Azure CLI installed (see [Azure CLI install steps](https://learn.microsoft.com/cli/azure/install-azure-cli) if needed)

## 1) Sign in to Azure CLI

```bash  theme={"theme":{"light":"min-light","dark":"min-dark"}}
az login # Sign in and select your Azure subscription
az extension add -n ssh # Extension required for Azure Bastion SSH management
```

## 2) Register required resource providers (one-time)

```bash  theme={"theme":{"light":"min-light","dark":"min-dark"}}
az provider register --namespace Microsoft.Compute
az provider register --namespace Microsoft.Network
```

Verify Azure resource provider registration. Wait until both show `Registered`.

```bash  theme={"theme":{"light":"min-light","dark":"min-dark"}}
az provider show --namespace Microsoft.Compute --query registrationState -o tsv
az provider show --namespace Microsoft.Network --query registrationState -o tsv
```

## 3) Set deployment variables

```bash  theme={"theme":{"light":"min-light","dark":"min-dark"}}
RG="rg-openclaw"
LOCATION="westus2"
TEMPLATE_URI="https://raw.githubusercontent.com/openclaw/openclaw/main/infra/azure/templates/azuredeploy.json"
PARAMS_URI="https://raw.githubusercontent.com/openclaw/openclaw/main/infra/azure/templates/azuredeploy.parameters.json"
```

## 4) Select SSH key

Use your existing public key if you have one:

```bash  theme={"theme":{"light":"min-light","dark":"min-dark"}}
SSH_PUB_KEY="$(cat ~/.ssh/id_ed25519.pub)"
```

If you don’t have an SSH key yet, run the following:

```bash  theme={"theme":{"light":"min-light","dark":"min-dark"}}
ssh-keygen -t ed25519 -a 100 -f ~/.ssh/id_ed25519 -C "you@example.com"
SSH_PUB_KEY="$(cat ~/.ssh/id_ed25519.pub)"
```

## 5) Select VM size and OS disk size

Set VM and disk sizing variables:

```bash  theme={"theme":{"light":"min-light","dark":"min-dark"}}
VM_SIZE="Standard_B2as_v2"
OS_DISK_SIZE_GB=64
```

Choose a VM size and OS disk size that are available in your Azure subscription/region and matches your workload:

* Start smaller for light usage and scale up later
* Use more vCPU/RAM/OS disk size for heavier automation, more channels, or larger model/tool workloads
* If a VM size is unavailable in your region or subscription quota, pick the closest available SKU

List VM sizes available in your target region:

```bash  theme={"theme":{"light":"min-light","dark":"min-dark"}}
az vm list-skus --location "${LOCATION}" --resource-type virtualMachines -o table
```

Check your current VM vCPU and OS disk size usage/quota:

```bash  theme={"theme":{"light":"min-light","dark":"min-dark"}}
az vm list-usage --location "${LOCATION}" -o table
```

## 6) Create the resource group

```bash  theme={"theme":{"light":"min-light","dark":"min-dark"}}
az group create -n "${RG}" -l "${LOCATION}"
```

## 7) Deploy resources

This command applies your selected SSH key, VM size, and OS disk size.

```bash  theme={"theme":{"light":"min-light","dark":"min-dark"}}
az deployment group create \
  -g "${RG}" \
  --template-uri "${TEMPLATE_URI}" \
  --parameters "${PARAMS_URI}" \
  --parameters location="${LOCATION}" \
  --parameters vmSize="${VM_SIZE}" \
  --parameters osDiskSizeGb="${OS_DISK_SIZE_GB}" \
  --parameters sshPublicKey="${SSH_PUB_KEY}"
```

## 8) SSH into the VM through Azure Bastion

```bash  theme={"theme":{"light":"min-light","dark":"min-dark"}}
RG="rg-openclaw"
VM_NAME="vm-openclaw"
BASTION_NAME="bas-openclaw"
ADMIN_USERNAME="openclaw"
VM_ID="$(az vm show -g "${RG}" -n "${VM_NAME}" --query id -o tsv)"

az network bastion ssh \
  --name "${BASTION_NAME}" \
  --resource-group "${RG}" \
  --target-resource-id "${VM_ID}" \
  --auth-type ssh-key \
  --username "${ADMIN_USERNAME}" \
  --ssh-key ~/.ssh/id_ed25519
```

## 9) Install OpenClaw (in the VM shell)

```bash  theme={"theme":{"light":"min-light","dark":"min-dark"}}
curl -fsSL https://openclaw.ai/install.sh -o /tmp/openclaw-install.sh
bash /tmp/openclaw-install.sh
rm -f /tmp/openclaw-install.sh
openclaw --version
```

The installer script handles Node detection/installation and runs onboarding by default.

## 10) Verify the Gateway

After onboarding completes:

```bash  theme={"theme":{"light":"min-light","dark":"min-dark"}}
openclaw gateway status
```

Most enterprise Azure teams already have GitHub Copilot licenses. If that is your case, we recommend choosing the GitHub Copilot provider in the OpenClaw onboarding wizard. See [GitHub Copilot provider](/providers/github-copilot).

The included ARM template uses Ubuntu image `version: "latest"` for convenience. If you need reproducible builds, pin a specific image version in `infra/azure/templates/azuredeploy.json` (you can list versions with `az vm image list --publisher Canonical --offer ubuntu-24_04-lts --sku server --all -o table`).

## Next steps

* Set up messaging channels: [Channels](/channels)
* Pair local devices as nodes: [Nodes](/nodes)
* Configure the Gateway: [Gateway configuration](/gateway/configuration)
* For more details on OpenClaw Azure deployment with the GitHub Copilot model provider: [OpenClaw on Azure with GitHub Copilot](https://github.com/johnsonshi/openclaw-azure-github-copilot)


Built with [Mintlify](https://mintlify.com).