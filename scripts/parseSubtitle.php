<?php

$string = file_get_contents("/Users/aslihanozmen/Documents/dataset/en/dataset.json");
$json_a = json_decode($string, true);


foreach ($json_a as $subtitle => $subtitle_a) {
	echo $subtitle_a['id']. ' '.$subtitle_a['prompt'];
    echo "\r\n";
}

?>