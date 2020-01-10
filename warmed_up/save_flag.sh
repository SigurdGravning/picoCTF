#!/bin/bash

syntax=$(history | sed 's/   [0-9]*  //' | tail -n2 | head -n1)

cat << EOF > get_flag.sh
#!/bin/bash

${syntax}
EOF

chmod +x get_flag.sh
./get_flag.sh > flag.txt