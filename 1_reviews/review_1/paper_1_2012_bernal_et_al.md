BERNAL, Jorge; SÁNCHEZ, Javier; VILARINO, Fernando. Towards automatic polyp detection with a polyp appearance model. Pattern Recognition, v. 45, n. 9, p. 3166-3182, 2012.


---


Related work (as main paper, this will guide me in my research):
===

In the case of polyp detection, the bibliography can be divided into two categories:

- Polyp detection by means of shape descriptors; and
	- _Shape descriptors is not our focus for now..._
- Polyp detection by means of **texture (and color) descriptors**:
	- Concepts to study:
		- Texture.
		- Color.
	- Works to reproduce (if possible):
		1. P. Li, K. Chan, S. Krishnan, Learning a multi-size
		   patch-based hybrid kernel machine ensemble for abnormal region
		   detection in colonoscopic images, 2005 IEEE Computer Society Conference on
		   Computer Vision and Pattern Recognition (CVPR’05) (2005).
		2. **S. Ameling, S. Wirth, D. Paulus, G. Lacey, F.  Vilariño,
		   Texture-based polyp detection in colonoscopy, Bildverarbeitung f¨ur
		   die Medizin 2009 (2009) 346–350. _[in progress: study, reproduction, contributions]_**
		3. Karkanis, S.A. and Iakovidis, D.K. and Maroulis, D.E. et al.,
		   Computer-aided tumor detection in endoscopic video using color
		   wavelet features, Information Technology in Biomedicine, IEEE Transactions on 7
		   (2003) 141–152.
		4. M. Tjoa, S. Krishnan, Feature extraction for the analysis of colon
		   status from the endoscopic images, BioMedical Engineering OnLine 2
		   (2003) 
		5. M. Coimbra, J. Cunha, MPEG-7 visual descriptors and contributions
		   for automated feature extraction in capsule endoscopy, Circuits and
		   Systems for Video Technology, IEEE Transactions on 16 (2006) 628–637.
		6. Bernal, J. and Vilariñoo, F. and Sánchez, J., Feature Detectors and
		   Feature Descriptors: Where We Are Now, Technical Report 154,
		   Computer Vision Center & Computer Science Department Universitat Autònoma de
		   Barcelona, 2010.


Useful questions
===

**Status**: 4/7 Sections

Research questions and reason for the study:
---

This study tries to develop a model of polyp appearance that makes polyp detection automatic.
Regions of interest are segmented, followed by specific descriptions and its consequent classification.

- Reduction of miss rate.
- Add significant value to the colonoscopy procedure by means of CAD.

Basically, from analysis of colonoscopy images to auxiliary diagnostic.

Hypothesis or hypotheses tested:
---

Fact: intensity valleys appear to surround polyps as the light of the
colonoscope and the camera are in the same direction.

Hipothesis: valley and ridge information as cue to detect polyps.
    - Look for several cues to guide a model formation.

Extendend work? See ref 8 in paper.

How the hypothesis was tested:
---

Three stages: region segmentation, region description and region
classification.

First contribution: region segmentation stage, in which a image is decomposed
in a minimum number of informative region parts. One of these contains a polyp
in a complete way.
    - Input image -> Image preprocessing -> Image segmentation -> [Region
      Merging: Region information-based <--> Depth of valleys-based] -->
      Segmented image

Second contribution: introduction of the Sector Accumulation--Depth of Valleys
Accumulation (SA-DOVA).

The findings:
---



How the findings were interpreted:
---



---

How does the design of the study address the research questions?

How convicing are the results? Are any of the results surprising?

What does this study contribute toward answering the original question?

What aspects of the original question remain unanswered?

---

Tips:

1. Takes notes in your own words.

---

Summary:

1. State the research question and explain why it is interesting.
2. State the hypotheses tested.
3. Briefly describe the methods (design, participants, materials, procedure,
   what was manipulated [independent variables], what was measured [dependent
   variables], how data were analyzed.
4. Describe the results. Were they significant?
5. Explain the key implications of the results. Avoid overstating the
   importance of the findings.
6. The results, and the interpretation of the results, should relate directly
   to the hypothesis.

- Focus on content. Condense later as needed.
