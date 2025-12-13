#!/bin/bash

TARGET_DIR="/usr/lib/zabbix/externalscripts"
REPO_URL="https://github.com/victorsarkisyan/APIs.git"

# Temporary clone directory
TMP_DIR="$(mktemp -d)"

# Clone shallow copy
git clone --depth=1 "$REPO_URL" "$TMP_DIR" >/dev/null 2>&1

# Copy contents into externalscripts
rsync -a --delete "$TMP_DIR"/ "$TARGET_DIR"/

# Remove temp directory
rm -rf "$TMP_DIR"

#Give permissions to Zabbix
chown -R zabbix:zabbix /usr/lib/zabbix/externalscripts
chmod -R +x /usr/lib/zabbix/externalscripts
