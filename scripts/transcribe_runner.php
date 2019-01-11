<?php
$command = escapeshellcmd("python transcribe.py gs://asraudiofiles/FrenchGrp2-16K/fr-sb-696.wav");
$output =  shell_exec($command);
echo $output;
?>