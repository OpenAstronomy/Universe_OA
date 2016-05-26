#!/bin/bash
set -e

if [[ $TRAVIS_PULL_REQUEST == false && $TRAVIS_BRANCH == 'master' ]]; then
    echo "Will push to ghpages"
    echo "pushing the run branch"
    git push origin run
    echo " pushing the website"
    git push -f origin gh-pages
fi

