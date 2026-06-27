# Dataset-1

This repository contains four primary data files:

## Top-view video   
  * Video recording of the experiment from above the embankment.
  * A long format video used for data processing.
  * A 30 second format video used for presentations.

## Side-view video  
  * Video recording of the experiment from the side of the embankment.

## Electrical potential measurements  
  * Time-series electrical potential measurements from the wireless sensing spike packages.

## Resistance measurements 
  * Time-series resistance values calculated from the measured electrical potential. These resistance values are the primary processed sensor data used for soil saturation mapping and analysis.

  ![The data from all 9 sensor nodes converted into resistance and plotted as a time series. Key timestamps are highlighted by vertical lines.](9resistance-vs-time.jpg)
  
## Notes on videos provided
  * Brief frame jumps occur where camera batteries were changed during the test.
  * The camera slowly shifted/slid over the course of the recording.
  * Both videos were trimmed to a consistent 90-minute duration.
  * Original source video files were approximately 100 GB and were too large to include directly in the GitHub repository.
  * The video was exported from Kdenlive as a reduced-frame-rate MP4 for repository storage.
  * The exported version uses a low frame rate of 0.3333 frame per second to reduce file size while preserving the full video duration and original spatial resolution.
  * Audio was removed from the exported file to further reduce file size.
  * The video was encoded using H.264/MP4 settings in Kdenlive.
  * Average bitrate encoding was used, with the video bitrate set to 850K to reduce file size while preserving usable visual quality.
  * The resulting file plays correctly in VLC Media Player, but may not open in Microsoft/Windows Media Player due to codec or low-frame-rate compatibility limitations.
  