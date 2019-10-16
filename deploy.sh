#!/bin/bash

source .env

eval "$(ssh-agent -s)" # Start ssh-agent cache
chmod 600 keychain/travis_id_rsa # Allow read access to the private key
ssh-add keychain/travis_id_rsa # Add the private key to SSH

git config --global push.default matching
git remote add deploy ssh://$DEPLOY_USER@$DEPLOY_HOST:$DEPLOY_PORT$DEPLOY_DIR
git push deploy master

# Skip this command if you don't need to execute any additional commands after deploying.
# ssh apps@$IP -p $PORT <<EOF
#   cd $DEPLOY_DIR
#   crystal build --release --no-debug index.cr # Change to whatever commands you need!
# EOF



