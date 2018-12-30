Group 2 : 
Arpan Mukherjee MT17007
Kunal Suryavanshi MT17023
Shubhi Tiwari MT17057
--------------------------
All code in folder named 'code'
/preprocessing
	- mergeData.py - to merge subtitles from (say 5 videos) in to segments
	- timing.py - to make timing of merged srts continuous
	- nounIdentify.py - extracting nouns
/evaluation 
	- eval.py - generate ground truth topics from video headings and timing information from srt content
		  - precison, recall measures computed ( but later done manually as explained in report )
/model
	- videoindexing.py - tree based LDA model for indexing videos. 
			   - takes as input the merged srt file. and outputs the topics with timing information (indexes on the video)	