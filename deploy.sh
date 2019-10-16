#!/bin/bash

source .env

eval "$(ssh-agent -s)" # Start ssh-agent cache
chmod 600 keychain/travis_id_rsa # Allow read access to the private key
ssh-add keychain/travis_id_rsa # Add the private key to SSH

git config --global push.default matching
git remote add deploy ssh://$DEPLOY_USER@$DEPLOY_HOST:$DEPLOY_PORT$DEPLOY_DIR
git push deploy "${1:-master}"


if [ -z "$encrypted_a1430f60b6d9_iv" ]
then
      echo '$encrypted_a1430f60b6d9_iv is empty'
else
      echo '$encrypted_a1430f60b6d9_iv is NOT empty'
fi

ssh $DEPLOY_USER@$DEPLOY_HOST -p $DEPLOY_PORT <<EOF
  cd $DEPLOY_DIR
  openssl aes-256-cbc -K $encrypted_a1430f60b6d9_key -iv $encrypted_a1430f60b6d9_iv -in secrets.tar.enc -out secrets.tar -d
  tar xvf secrets.tar  
  make prod-run-new
EOF