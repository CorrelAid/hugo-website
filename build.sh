#!/bin/bash
if [ $CONTEXT = "production" ]
then
  echo "On main branch"
  hugo
else
  hugo -b $DEPLOY_PRIME_URL
fi
