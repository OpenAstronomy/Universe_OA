
#!/bin/bash
set -e

if [[ $TRAVIS_PULL_REQUEST == false && $TRAVIS_BRANCH == 'master' ]]; then
    echo "Will push to ghpages"
    chmod 600 $SSH_KEY
    eval `ssh-agent -s`
    ssh-add $SSH_KEY
    echo "pushing the run branch"
    git push upstream run
    echo " pushing the website"
    git push -f upstream gh-pages
fi

