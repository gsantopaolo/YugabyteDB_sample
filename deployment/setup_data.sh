# chmod +x setup_data.sh
# sudo ./setup_data.sh
set -euo pipefail
# Base directory: ../data/yugabytedb relative to this script's location
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BASE_DIR="$SCRIPT_DIR/../data/yugabytedb"

# Ensure the parent directory exists
mkdir -p "$BASE_DIR"

for i in 1 2 3; do
  DIR="$BASE_DIR/node$i"
  if [[ ! -d "$DIR" ]]; then
    echo "Creating $DIR"
    mkdir -p "$DIR"
  fi
  echo "Setting permissions 777 on $DIR"
  chmod 777 "$DIR"
done

DIR="$BASE_DIR/single-node"
if [[ ! -d "$DIR" ]]; then
  echo "Creating $DIR"
  mkdir -p "$DIR"
fi
echo "Setting permissions 777 on $DIR"
chmod 777 "$DIR"

echo "All nodes are ready under $BASE_DIR"

