#!/bin/bash

echo "$TEST_VAR"

git config --global push.default matching
git remote add deploy ssh://$DEPLOY_USER@$DEPLOY_HOST:$DEPLOY_PORT$DEPLOY_DIR
git push deploy "${1:-master}"

# https://blog.fortrabbit.com/deploying-code-with-rsync
# rsync -r --delete-after --quiet $TRAVIS_BUILD_DIR/keychain $DEPLOY_USER@$DEPLOY_HOST:$DEPLOY_PORT$DEPLOY_DIR

rsync -arvz -e \'"ssh -p $DEPLOY_PORT"\' --progress --delete-after $TRAVIS_BUILD_DIR/.env $DEPLOY_USER@$DEPLOY_HOST:$DEPLOY_DIR
rsync -arvz -e \'"ssh -p $DEPLOY_PORT"\' --progress --delete-after $TRAVIS_BUILD_DIR/keychain $DEPLOY_USER@$DEPLOY_HOST:$DEPLOY_DIR


ssh $DEPLOY_USER@$DEPLOY_HOST -p $DEPLOY_PORT <<EOF
  cd $DEPLOY_DIR
  make prod-run-new
EOF