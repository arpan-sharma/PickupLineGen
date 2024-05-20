#!/bin/sh

git filter-branch --env-filter '
if [ "$GIT_COMMITTER_EMAIL" = "arpansharma256@gmail.com" ];
then
    GIT_COMMITTER_NAME="Arpan Sharma";
    GIT_COMMITTER_EMAIL="85667417+arpan-sharma@users.noreply.github.com";
fi
if [ "$GIT_AUTHOR_EMAIL" = "arpansharma256@gmail.com" ];
then
    GIT_AUTHOR_NAME="Arpan Sharma";
    GIT_AUTHOR_EMAIL="85667417+arpan-sharma@users.noreply.github.com";
fi
' --tag-name-filter cat -- --branches --tags
