#!/bin/bash
#SBATCH --job-name=blender_flower
#SBATCH --output=blender.out
#SBATCH --error=blender.err
#SBATCH --array=1-100
#SBATCH --time=00:30:0
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=1GB
#SBATCH -p plgrid
#SBATCH -A plglscclass24-cpu

module load blender

BLEND_FILE="repeat_zone_flower_by_MiRA.blend"
OUTPUT_DIR="$SCRATCH/rendered_frames"

mkdir -p $OUTPUT_DIR

blender -b "$BLEND_FILE" -o "$OUTPUT_DIR/frame_" -F PNG -f $SLURM_ARRAY_TASK_ID

# Notify completion
echo "Rendering completed for frame $SLURM_ARRAY_TASK_ID. Results are in $OUTPUT_DIR"