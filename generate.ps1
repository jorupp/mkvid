# generate text file from a video for use with https://github.com/Rightpoint/fireworks2021/blob/main/examples/rupp-extra.py

$inFile = "E:\downloads\original downloads\input.mp4"
$ffmpeg = "C:\utilities\ffmpeg\bin\ffmpeg.exe"
$outFolder = "output"
# https://video.stackexchange.com/a/4571
# -filter:v "crop=out_w:out_h:x:y"

mkdir $outFolder

#& $ffmpeg -i $input -r 30 -ss 00:00:45 -to 00:00:47 $outFolder/file-%03d.png
& $ffmpeg -i $inFile -r 30 -ss 00:01:09 -to 00:01:12 -filter:v "crop=1450:750:250:200,scale=w=29:h=15" $outFolder/file-%03d.png
#& $ffmpeg -i $inFile -r 30 -ss 00:01:09 -to 00:01:12 -filter:v "crop=1600:750:200:200" $outFolder/file-%03d.png

Remove-Item $outFolder\file-001.png
Remove-Item $outFolder\file-002.png
Remove-Item $outFolder\file-003.png

python.exe build-file.py