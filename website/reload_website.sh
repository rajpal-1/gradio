#!/bin/sh
. /home/ubuntu/.bashrc
export PATH="/usr/local/bin:/usr/bin:/bin"

git pull > /tmp/git_changes.txt

if grep -q "Already up to date." /tmp/git_changes.txt; then
    echo "Already up to date. No reload."
else
    if grep -q "error" /tmp/git_changes.txt; then
        LOGS=`cat /tmp/git_changes.txt`
        curl -X POST -H 'Content-type: application/json' --data '{"text":":o: gradio.app is not tracking master\n\n Logs:\n```'"${LOGS}"'`"}' ${SLACK_WEBHOOK}
    fi
    echo "Reloading..."
    if grep -q "demo/" /tmp/git_changes.txt; then
        cd upload_notebooks && python run.py && cd ..
    fi
    if docker-compose build && docker-compose up -d ; then
        LATEST=$(git log -1 | fgrep commit)$(git log -1 | tail -1)
        curl -X POST -H 'Content-type: application/json' --data '{"text":"gradio.app relaoded successfully! :ship:
        \n\nLatest:\n>`'"${LATEST}"'`"}' ${SLACK_WEBHOOK}
    else
        LOGS=$(tail -n 25 /var/mail/ubuntu)
        curl -X POST -H 'Content-type: application/json' --data '{"text":":o: gradio.app is not tracking master\n\nLogs:\n```'"${LOGS}"'`"}' ${SLACK_WEBHOOK}
    fi
fi