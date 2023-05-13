import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

env_KV = os.environ["env_cosmos_endpoint"]
env_tenant_id = os.environ["env_cosmos_key"]
env_client_id = os.environ["env_openai_key"]
env_client_secret = os.environ["env_api_base"]

m_strKVUri = f"https://{env_KV}.vault.azure.net"

credential = DefaultAzureCredential()
client = SecretClient(vault_url=m_strKVUri, credential=credential)


from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient

credential = ClientSecretCredential(
    tenant_id=env_tenant_id, client_id=env_client_id, client_secret=env_client_secret
)

client = SecretClient(vault_url=m_strKVUri, credential=credential)

secret = client.get_secret("main")
print(secret.value)
