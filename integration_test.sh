rm -f ./ged/optimus_prime.ged
for f in ./ged/*; do (cat "${f}"; echo) | grep '\S' >> ./ged/optimus_prime.ged; done
python index.py