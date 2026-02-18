#!/usr/bin/env bash
set -euo pipefail

REPO="https://github.com/jaosullivan/django-gitops.git"
DIR="django-gitops"
CHART="apps/django-app"
COLOR="$1"

if [[ "$COLOR" != "blue" && "$COLOR" != "green" ]]; then
  echo "Color must be blue or green"
  exit 1
fi

rm -rf "$DIR"
git clone "$REPO" "$DIR"
cd "$DIR"

yq -i ".service.activeColor = \"$COLOR\"" "$CHART/values.yaml"

git config user.email "ci@jenkins"
git config user.name "Jenkins CI"

git add "$CHART/values.yaml"
git commit -m "Switch active color to $COLOR"
git push