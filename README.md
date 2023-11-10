# Pypipe

This project use with same repositories

The project to use for clone repository
-  https://github.com/guilhermelinhares/golang_example

The project to use for deploy secrets in vault

- https://github.com/guilhermelinhares/vault_config


# Run project

Environment Varibles for Example:

```hcl
export APP_NAME='exemplo'
export DEFAULT_TECHNOLOGY=java
export ROLE_ID="..."
export SECRET_ID="...."
export ENVIRONMENT=dev
export BRANCH_TAG='main'
export APP_NAME_GIT='golang_example'
export GIT_PROJECT=guilhermelinhares 
```

Install requirements

-  pip install --user -r requirements.txt

Run deploy

- python3 __init__.py 