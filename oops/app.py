# create a class for load arguments

from deploy_tools import (
    deploy_utils
)

secret = deploy_utils.Genpassword()
print(secret.get_secret())
