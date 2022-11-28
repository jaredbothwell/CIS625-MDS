
for i in 1 
do 
    for j in 300
    do
        sbatch sbatch.sh $i 5000 $j
    done
done