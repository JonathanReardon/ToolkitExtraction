---
title: "Summary.Rmd"
author: "Jonathan Reardon"
output:
  html_document:
    keep_md: true
    df_print: paged
  #pdf_document: default
editor_options:
  chunk_output_type: inline
---


```r
library(reticulate)
library(ggplot2)
library(dplyr)
library(reshape2)
library(gridExtra)
use_python("/usr/local/bin/python3")
```


```python
# import necessary libraries
import json
from collections import Counter
from pprint import pprint
from matplotlib import pyplot as plt
import pandas as pd
plt.style.use('ggplot')

# import dataset
with open('/home/jon/json/Batch1.json') as f:
    data=json.load(f)
    
###################################################
### GET STRAND LABELS AND KEYS FROM TOP OUTER LAYER
###################################################

def get_strand_info():
    ''' 
    a function that returns
    a dict containing strand labels
    and corresponding attribute ids
    '''
    strands={}
    for counter, element in enumerate(data["CodeSets"][0]["Attributes"]["AttributesList"]):
        attribute_name=(data["CodeSets"][0]["Attributes"]["AttributesList"][counter]["AttributeName"])
        attribute_id=(data["CodeSets"][0]["Attributes"]["AttributesList"][counter]["AttributeId"])
        strands.update( {attribute_id:attribute_name} )
    return strands
    
######################################
### DISPLAY STRAND SUMMARY INFORMATION 
######################################
    
def get_strand_summary():
    '''
    A function that produces a basic
    summary of strand study counts
    and a graph to display them
    '''
    global counts, strand_title
    strand_overview=[]
    for element in range(len(data["References"])):
        for key, value in strands.items():
          if "Codes" in data["References"][element]:
            for section in range(len(data["References"][element]["Codes"])):
                if key == data["References"][element]["Codes"][section]["AttributeId"]:
                    a=(data["References"][element]["ItemId"])
                    b=(data["References"][element]["Title"])
                    strand_overview.append([value, key, a, b])

    strand_title=[]
    for element in strand_overview:
        strand_title.append(element[0])

    counts = Counter(strand_title) 
    pprint(counts)

######################################################
###  GET INFO FROM STRAND SPECIFIC STUDIES
######################################################

def get_data():
    '''
    A function that accepts a strand id and a variable of
    interest and returns a list of that id and the variable
    values.
    '''
    outcome_studies=[] 

    # iterate over each section of 'references'
    for section in range(len(data["References"])):
        if "Codes" in data["References"][section]:
          for study in range(len(data["References"][section]["Codes"])):
              # check each study to see if strand id is present
              for item, value in strands.items():
                  if item == data["References"][section]["Codes"][study]["AttributeId"]:
                    shorttitle=(data["References"][section]["ShortTitle"])
                    year=(data["References"][section]["Year"])
                    studyID=(data["References"][section]["ItemId"])
                    outcome_studies.append([shorttitle, year, studyID, value])
              
  
    # convert data list to pandas dataframe for viewing
    df_primary = pd.DataFrame(outcome_studies, columns=['Author', 'Year', 'StudyID', 'Strand'])
    
    return df_primary
```


```python
strands = get_strand_info()
get_strand_summary()
```

```
## Counter({'Oral language interventions': 138,
##          'Feedback': 114,
##          'Peer tutoring': 109,
##          'Teaching assistants': 62,
##          'Small group tuition': 30,
##          'One to one tuition': 10,
##          'Phonics': 6,
##          'Digital technology': 4,
##          'Metacognition and self-regulation': 4,
##          'Parental engagement': 1,
##          'Extending school time': 1,
##          'Reducing class size': 1})
```


```python
pprint(strands)
```

```
## {5023544: 'Arts participation',
##  5023545: 'Aspiration interventions',
##  5023546: 'Behaviour interventions',
##  5023547: 'Block scheduling',
##  5023548: 'Peer tutoring',
##  5023549: 'Small group tuition',
##  5023550: 'Built environment',
##  5023551: 'Collaborative learning',
##  5023552: 'Digital technology',
##  5023553: 'Extending school time',
##  5023554: 'Early years intervention',
##  5023555: 'Feedback',
##  5023556: 'Homework',
##  5023557: 'Individualised instruction',
##  5023558: 'Learning styles',
##  5023559: 'Mastery learning',
##  5023560: 'Mentoring',
##  5023561: 'Metacognition and self-regulation',
##  5023562: 'One to one tuition',
##  5023563: 'Oral language interventions',
##  5023564: 'Outdoor adventure learning',
##  5023565: 'Parental engagement',
##  5023566: 'Performance pay',
##  5023567: 'Phonics',
##  5023568: 'Reading comprehension strategies',
##  5023569: 'Reducing class size',
##  5023570: 'Repeating a year',
##  5023571: 'School uniform',
##  5023572: 'Setting or streaming',
##  5023573: 'Social and emotional learning',
##  5023574: 'Sports participation',
##  5023575: 'Summer schools',
##  5023576: 'Teaching assistants'}
```


```python
data = get_data()
```


```r
all <- data.frame(py$data)
#View(all)
print(all)
```

```
##                       Author Year  StudyID                            Strand
## 1           Aarnoutse (1997) 1997 38111324       Oral language interventions
## 2           Aarnoutse (1998) 1998 38111325       Oral language interventions
## 3          Abbondanza (2013) 2013 37116221                     Peer tutoring
## 4               Adler (1998) 1998 37092570                          Feedback
## 5             Ahlfors (1979) 1979 38111424       Oral language interventions
## 6             Allsopp (1995) 1995 37133863                     Peer tutoring
## 7               Ammon (1971) 1971 38111471       Oral language interventions
## 8              Anders (1984) 1984 38111425       Oral language interventions
## 9            Anderson (1973) 1973 37092749                          Feedback
## 10            Andrade (2008) 2008 37092571                          Feedback
## 11            Aram (2004) OL 2004 38111637       Oral language interventions
## 12               Aram (2006) 2006 38111536       Oral language interventions
## 13          Arblaster (1991) 1991 37093532                     Peer tutoring
## 14          Armstrong (2000) 2000 38111426       Oral language interventions
## 15              Arter (1994) 1994 37092572                          Feedback
## 16           Atherley (1989) 1989 37093533                     Peer tutoring
## 17           Aumiller (1963) 1963 37061105                          Feedback
## 18            Baechie (1990) 1990 37092622                          Feedback
## 19              Baker (2005) 2005 37133865                     Peer tutoring
## 20              Banks (1987) 1987 38111556       Oral language interventions
## 21            Bar-Eli (1982) 1982 37093467                     Peer tutoring
## 22            Baumann (1992) 1992 38111328       Oral language interventions
## 23            Baumann (2002) 2002 38111427       Oral language interventions
## 24               Beck (1982) 1982 38111428       Oral language interventions
## 25               Beck (2007) 2007 38111473       Oral language interventions
## 26            Bennett (2013) 2013 37671594               Teaching assistants
## 27         Benson (1979) 1_1 1979 37092573                          Feedback
## 28         Benson (1979) 1_2 1979 40294885                          Feedback
## 29           Bereiter (1985) 1985 38111329       Oral language interventions
## 30             Bethge (1982) 1982 37092626                          Feedback
## 31            Biggart (2015) 2015 38296603                Digital technology
## 32            Biggart (2015) 2015 38296603               Teaching assistants
## 33             Bilsky (1978) 1978 37092628                          Feedback
## 34        Bingham (2010) SGT 2010 40294886               Small group tuition
## 35        Bingham (2010) SGT 2010 40294886                One to one tuition
## 36         Blatchford (2007) 2007 37671632               Teaching assistants
## 37              Block (1970) 1970 37092755                          Feedback
## 38              Block (2006) 2006 38111430       Oral language interventions
## 39             Bochna (2006) 2006 38111679       Oral language interventions
## 40       Boggiano (1985) 1_2 1985 40294887                          Feedback
## 41           Bohannon (1975) 1975 37091022                          Feedback
## 42               Bond (1967) 1967 38111600       Oral language interventions
## 43              Bonds (1987) 1987 38111474       Oral language interventions
## 44            Bortnem (2005) 2005 38111475       Oral language interventions
## 45                Bos (1990) 1990 38111431       Oral language interventions
## 46                Bos (1992) 1992 38111432       Oral language interventions
## 47         Boulet (1990) 1_1 1990 37092604                          Feedback
## 48         Boulet (1990) 1_2 1990 40294889                          Feedback
## 49                Box (1993) 1993 38111680       Oral language interventions
## 50            Brabham (2002) 2002 38111538       Oral language interventions
## 51              Brady (1990) 1990 38111333       Oral language interventions
## 52           Bramlett (1994) 1994 37093538                     Peer tutoring
## 53   Brandstetter (1978) 1_1 1978 37091024                          Feedback
## 54   Brandstetter (1978) 1_2 1978 40294890                          Feedback
## 55             Bridge (1983) 1983 38111601       Oral language interventions
## 56      Bridgeman (1974) 1_1 1974 37092631                          Feedback
## 57      Bridgeman (1974) 1_2 1974 40294891                          Feedback
## 58            Brimmer (2004) 2004 38111334       Oral language interventions
## 59          Brookhart (2008) 2010 37092605                          Feedback
## 60             Brooks (2006) 2006 38111478       Oral language interventions
## 61              Brown (2005) 2005 37671541               Teaching assistants
## 62              Bruno (2004) 2004 37133869                     Peer tutoring
## 63              Brush (1997) 1997 37093539                     Peer tutoring
## 64           Buchanan (2015) 2015 38296604               Small group tuition
## 65           Buchanan (2015) 2015 38296605               Small group tuition
## 66            Buckner (1978) 1978 38111602       Oral language interventions
## 67          Bumgarner (1984) 1984 37061108                          Feedback
## 68               Bunn (2008) 2008 37671596               Teaching assistants
## 69           Burgoyne (2012) 2012 37671542               Teaching assistants
## 70         Butler (1986) 1_1 1986 37092634                          Feedback
## 71         Butler (1986) 1_2 1986 40294895                          Feedback
## 72         Butler (1987) 1_1 1987 37092633                          Feedback
## 73         Butler (1987) 1_2 1987 40294893                          Feedback
## 74         Butler (1987) 1_3 1987 40294894                          Feedback
## 75      Caccamise (2007) 1_1 2007 37092575                          Feedback
## 76      Caccamise (2007) 1_2 2007 40294896                          Feedback
## 77            Calhoon (2003) 2003 37093518                     Peer tutoring
## 78           Carberry (2003) 2003 37116223                     Peer tutoring
## 79            Carlton (1985) 1985 37093351                     Peer tutoring
## 80             Carney (1984) 1984 38111434       Oral language interventions
## 81   Carriedo (1995)  OL 1_1 1995 38111338       Oral language interventions
## 82    Carriedo (1995) OL 1_2 1995 43090120       Oral language interventions
## 83            Cashman (1977) 1977 38111562       Oral language interventions
## 84             Center (1997) 1997 38111670       Oral language interventions
## 85     Chamberlain (1993) OL 1993 38111564       Oral language interventions
## 86                Chu (2017) 2017 37116229                     Peer tutoring
## 87             Clarke (2017) 2017 37671546               Teaching assistants
## 88            Cleland (1964) 1964 38111604       Oral language interventions
## 89                Coe (2011) 2011 37092576                          Feedback
## 90               Cole (2009) 2009 37671598               Teaching assistants
## 91          Cooper (2016) PT 2016 43090135                     Peer tutoring
## 92          Cooper (2016) TA 2016 37671620               Teaching assistants
## 93              Coyne (2004) 2004 38111644       Oral language interventions
## 94          Coyne (2007) 1_1 2007 38111643       Oral language interventions
## 95          Coyne (2007) 1_2 2007 40294900       Oral language interventions
## 96              Coyne (2010) 2010 38111435       Oral language interventions
## 97     Crain-Thoreson (1999) 1999 38111539       Oral language interventions
## 98             Craker (1981) 1981 37093542                     Peer tutoring
## 99         Crevecoeur (2008) 2008 38111484       Oral language interventions
## 100          Crutcher (1975) 1975 37091026                          Feedback
## 101         Davenport (1999) 1999 37093543                     Peer tutoring
## 102              Dion (2011) 2011 37093616                     Peer tutoring
## 103          Dockrell (2015) 2015 37671548               Teaching assistants
## 104              Dole (1995) 1995 38111436       Oral language interventions
## 105         Dorval (1978) TA 1978 43090143               Teaching assistants
## 106           Dubrule (1984) 1984 37091027                          Feedback
## 107              Duff (1974) 1974 37093544                     Peer tutoring
## 108              Duff (2014) 2014 37671600               Teaching assistants
## 109             Early (1998) 1998 37133886                     Peer tutoring
## 110             Eggen (1978) 1978 37092761                          Feedback
## 111       Ehlinger (1988) FB 1988 40294902                          Feedback
## 112       Ehlinger (1988) OL 1988 38111345       Oral language interventions
## 113              Ehri (2007) 2007 38878251               Small group tuition
## 114            Elliot (1986) 1986 37061114                          Feedback
## 115           Englert (1991) 1991 38111346       Oral language interventions
## 116           Englert (1994) 1994 38111347       Oral language interventions
## 117          Erickson (1972) 1972 37093353                     Peer tutoring
## 118             Ewers (1999) 1999 38111491       Oral language interventions
## 119          Fantuzzo (1992) 1992 37093472                     Peer tutoring
## 120          Fantuzzo (1995) 1995 37093471                     Peer tutoring
## 121         Feitelson (1986) 1986 38111288       Oral language interventions
## 122         Feitelson (1993) 1993 38111287       Oral language interventions
## 123              Fien (2011) 2011 38878265               Small group tuition
## 124            Fisher (2001) 2001 37093506                     Peer tutoring
## 125        Fitzgerald (1987) 1987 37092577                          Feedback
## 126       Fitz-Gibbon (1990) 1990 37133895                     Peer tutoring
## 127           Franzke (2005) 2005 37092578                          Feedback
## 128           Freeman (2008) 2008 38111492       Oral language interventions
## 129            Fricke (2013) 2013 37671552               Teaching assistants
## 130            Fricke (2017) 2017 37671553               Teaching assistants
## 131             Fuchs (1984) 1984 37091029                          Feedback
## 132             Fuchs (1989) 1989 37092579                          Feedback
## 133             Fuchs (1991) 1991 37092580                          Feedback
## 134             Fuchs (1991) 1991 37092581                          Feedback
## 135          Fuchs (1994) FB 1994 40294904                          Feedback
## 136             Fuchs (1995) 1995 37093553                     Peer tutoring
## 137             Fuchs (1997) 1997 37093549                     Peer tutoring
## 138             Fuchs (1997) 1997 37093550                     Peer tutoring
## 139             Fuchs (1997) 1997 37093524                     Peer tutoring
## 140             Fuchs (1998) 1998 37133902                     Peer tutoring
## 141             Fuchs (1999) 1999 37093618                     Peer tutoring
## 142             Fuchs (1999) 1999 37093551                     Peer tutoring
## 143             Fuchs (2001) 2001 37093523                     Peer tutoring
## 144             Fuchs (2002) 2002 37116212                     Peer tutoring
## 145         Gallagher (1975) 1975 38111608       Oral language interventions
## 146           Gardner (1973) 1973 37133906                     Peer tutoring
## 147           Gardner (1982) 1982 37093555                     Peer tutoring
## 148           Gherfal (1982) 1982 37061127                          Feedback
## 149             Gibbs (2001) 2001 37671623               Teaching assistants
## 150    Ginsburg-Block (1997) 1997 37093477                     Peer tutoring
## 151    Ginsburg-Block (1998) 1998 37093478                     Peer tutoring
## 152           Glaeser (1998) 1998 38111355       Oral language interventions
## 153            Glover (1989) 1989 37092650                          Feedback
## 154           Gmitter (1989) 1989 37133911                     Peer tutoring
## 155             Goetz (2008) 2008 37671603               Teaching assistants
## 156            Gorard (2014) 2014 38296617               Teaching assistants
## 157            Gorard (2014) 2014 38296617                One to one tuition
## 158            Gorard (2015) 2015 38296614       Oral language interventions
## 159            Gorard (2015) 2015 38296614 Metacognition and self-regulation
## 160            Gorard (2015) 2015 38296615                Digital technology
## 161            Gorard (2015) 2015 38296615                          Feedback
## 162            Gorard (2015) 2015 38296616               Small group tuition
## 163            Gorard (2015) 2015 38296616                           Phonics
## 164         Gottshall (2007) 2007 38878252               Small group tuition
## 165             Goyen (1994) 1994 37093559                     Peer tutoring
## 166            Graham (2007) 2007 37671634               Teaching assistants
## 167          Graup (1985) OL 1985 38111575       Oral language interventions
## 168            Graves (2010) 2010 37671557               Teaching assistants
## 169              Gray (2007) 2007 37671558               Teaching assistants
## 170         Greenwood (1989) 1989 37093560                     Peer tutoring
## 171             Gregg (1994) 1994 37133917                     Peer tutoring
## 172         Guastello (2001) 2001 37092582                          Feedback
## 173         Guastello (2001) 2001 37092582               Parental engagement
## 174    Gudbrandsen (2005) PT 2005 37133918                     Peer tutoring
## 175          Guerrero (2015) 2015 37671515               Teaching assistants
## 176              Gunn (2005) 2005 38878253               Small group tuition
## 177     Gwernan-Jones (2018) 2018 37671559               Teaching assistants
## 178            Hafner (1965) 1965 38111437       Oral language interventions
## 179              Hahn (1966) 1966 38111610       Oral language interventions
## 180             Haley (2017) 2017 37671520               Teaching assistants
## 181            Hanley (2015) 2015 38296621       Oral language interventions
## 182            Hanley (2015) 2015 38296621 Metacognition and self-regulation
## 183             Hanna (1976) 1976 37092655                          Feedback
## 184            Hannah (2008) 2008 37133919                     Peer tutoring
## 185         Hardegree (2012) 2012 37116213                     Peer tutoring
## 186          Hargrave (2000) 2000 38111647       Oral language interventions
## 187            Haring (1975) 1975 37091033                          Feedback
## 188            Harris (1966) 1966 38111612       Oral language interventions
## 189            Harvey (2002) 2002 38111494       Oral language interventions
## 190            Hasson (1981) 1981 38111495       Oral language interventions
## 191           Hatcher (2006) 2006 37671562               Teaching assistants
## 192             Hedin (2008) 2008 38111363       Oral language interventions
## 193            Heller (1992) 1992 37093480                     Peer tutoring
## 194            Hilger (2000) 2000 37133921                     Peer tutoring
## 195            Hodgen (2019) 2019 40398941               Teaching assistants
## 196            Hodgen (2019) 2019 40398941                One to one tuition
## 197        Hoisington (1968) 1968 38111439       Oral language interventions
## 198            Holman (2011) 2011 37092584                          Feedback
## 199            Holmes (2013) 2013 37671521               Teaching assistants
## 200            Howard (1992) 1992 38111577       Oral language interventions
## 201            Hughes (1973) 1973 37092768                          Feedback
## 202         Hund-Reid (2008) 2008 37671626               Teaching assistants
## 203         Hund-Reid (2013) 2013 37671605               Teaching assistants
## 204             Hymel (1980) 1980 37061117                          Feedback
## 205            Inglis (2002) 2002 37133923                     Peer tutoring
## 206           Jackson (1963) 1963 38111440       Oral language interventions
## 207           Jackson (2016) 2016 37116224                     Peer tutoring
## 208            Jacobs (1966) 1966 37061115                          Feedback
## 209          Jacobson (2001) 2001 37093509                     Peer tutoring
## 210             Jason (1994) 1994 37671565               Teaching assistants
## 211             Jason (1994) 1994 37671565                One to one tuition
## 212               Jay (2017) 2017 38296628       Oral language interventions
## 213        Jenkins (1991) PT 1991 40294914                     Peer tutoring
## 214            Jewell (2003) 2003 37092585                          Feedback
## 215             Jones (1984) 1984 38111441       Oral language interventions
## 216             Jones (2016) 2016 37671627               Teaching assistants
## 217           Justice (2005) 2005 38111649       Oral language interventions
## 218           Justice (2010) 2010 38111681       Oral language interventions
## 219              Kahl (1994) 1994 37093568                     Peer tutoring
## 220      Kameenui (1982) 1_1 1982 38111442       Oral language interventions
## 221      Kameenui (1982) 1_2 1982 40294915       Oral language interventions
## 222     Karagiannakis (2008) 2008 37116222                     Peer tutoring
## 223           Karweit (1989) 1989 38111673       Oral language interventions
## 224          Kendrick (1966) 1966 38111615       Oral language interventions
## 225            Kertoy (1994) 1994 38111543       Oral language interventions
## 226             Khare (1992) 1992 38111290       Oral language interventions
## 227               Kim (2002) 2002 38111578       Oral language interventions
## 228              King (1983) 1983 37091034                          Feedback
## 229              King (2003) 2003 37092606                          Feedback
## 230              King (2015) 2015 38296632               Small group tuition
## 231              King (2015) 2015 38296632                           Phonics
## 232          Kinnunen (1995) 1995 38111371       Oral language interventions
## 233          Kitmitto (2018) 2018 40398942 Metacognition and self-regulation
## 234          Kitmitto (2018) 2018 40398942       Oral language interventions
## 235         Koedinger (2010) 2010 37092607                          Feedback
## 236  Kolic-Vehovec (2002) FB 2002 40294919                          Feedback
## 237             Korat (2007) 2007 38111650       Oral language interventions
## 238            Kozlow (2004) 2004 37092586                          Feedback
## 239      Kramarski (2009) FB 2009 40294920                          Feedback
## 240           Kux-Cox (1974) 1974 38111444       Oral language interventions
## 241            Lacher (1983) 1983 37092670                          Feedback
## 242              Lamb (1971) 1971 38111617       Oral language interventions
## 243              Lamb (1986) 1986 38111499       Oral language interventions
## 244           Lamport (1982) 1982 37093356                     Peer tutoring
## 245               Lee (2016) 2016 37671606               Teaching assistants
## 246            Lennon (1999) 1999 38878267               Small group tuition
## 247             Leung (2008) 2008 38111674       Oral language interventions
## 248                Li (1996) 1996 38111380       Oral language interventions
## 249         Lieberman (1965) 1965 38111445       Oral language interventions
## 250             Lloyd (2015) 2015 38296633                     Peer tutoring
## 251             Lloyd (2015) 2015 38296634                     Peer tutoring
## 252           Lonigan (1998) 1998 38111652       Oral language interventions
## 253           Lonigan (1999) 1999 38111651       Oral language interventions
## 254          Loranger (1997) 1997 38111381       Oral language interventions
## 255            Lovett (1996) 1996 38111382       Oral language interventions
## 256     Lowenthal (1981) SGT 1981 40294923               Small group tuition
## 257             Lucas (2006) 2006 38111508       Oral language interventions
## 258          Lumbelli (1999) 1999 37092587                          Feedback
## 259         MacArthur (1991) 1991 37092588                          Feedback
## 260           MacLeod (2007) 2007 37671566               Teaching assistants
## 261             Mason (1990) 1990 38111683       Oral language interventions
## 262            Mathes (1993) 1993 37093622                     Peer tutoring
## 263            Mathes (1998) 1998 37093577                     Peer tutoring
## 264            Mathes (2001) 2001 37116235                     Peer tutoring
## 265            Mathes (2003) 2003 37116234                     Peer tutoring
## 266        Mathes (2005) 1_1 2005 38878258               Small group tuition
## 267        Mathes (2005) 1_2 2005 40294924               Small group tuition
## 268            Mautte (1990) 1990 38111684       Oral language interventions
## 269           Maxwell (2015) 2015 38296641       Oral language interventions
## 270        McClintock (1975) 1975 37092684                          Feedback
## 271         McCracken (1979) 1979 37093360                     Peer tutoring
## 272           McKeown (1983) 1983 38111446       Oral language interventions
## 273           McKeown (1985) 1985 38111447       Oral language interventions
## 274   McKeown (2009)  OL 1_1 2009 38111387       Oral language interventions
## 275   McKeown (2009)  OL 1_2 2009 40294925       Oral language interventions
## 276 McNally (2016) Study 1_1 2016 37671568               Teaching assistants
## 277 McNally (2016) Study 1_1 2016 37671568               Small group tuition
## 278              Medo (1993) 1993 38111448       Oral language interventions
## 279          Menesses (2009) 2009 37133945                     Peer tutoring
## 280           Merrell (2015) 2015 37671570               Teaching assistants
## 281           Merrell (2015) 2015 37671570                           Phonics
## 282        Merrett (1996) FB 1996 40294926                          Feedback
## 283           Merrill (2002) 2002 37133947                     Peer tutoring
## 284          Mevarech (1991) 1991 37093581                     Peer tutoring
## 285          Mevarech (1993) 1993 37093579                     Peer tutoring
## 286             Meyer (2010) 2010 37092589                          Feedback
## 287            Miller (2003) 2003 37671572               Teaching assistants
## 288           Miranda (1997) 1997 38111389       Oral language interventions
## 289            Mirkin (1979) 1979 37091036                          Feedback
## 290         Mooney (1986) PT 1986 43090186                     Peer tutoring
## 291         Moore (1961) 1_1 1961 37061123                          Feedback
## 292         Moore (1961) 1_2 1961 40294931                          Feedback
## 293          Moore (1993) PT 1993 40294930                     Peer tutoring
## 294         Morrow (1984) OL 1984 38111653       Oral language interventions
## 295        Morrow (1985) 1_1 1985 38111675       Oral language interventions
## 296        Morrow (1985) 1_2 1985 40294932       Oral language interventions
## 297            Morrow (1988) 1988 38111676       Oral language interventions
## 298            Morrow (1989) 1989 38111549       Oral language interventions
## 299            Morrow (1990) 1990 38111291       Oral language interventions
## 300            Morrow (1992) 1992 38111677       Oral language interventions
## 301             Muijs (2003) 2003 37671607               Teaching assistants
## 302            Murphy (2007) 2007 38111512       Oral language interventions
## 303         Naseerali (2013) 2013 37116214                     Peer tutoring
## 304              Nash (2006) 2006 38111449       Oral language interventions
## 305        Neenan (1986) 1_1 1986 37092701                          Feedback
## 306         Nelson (2003) OL 2003 38111390       Oral language interventions
## 307            Nelson (2010) 2010 37671575               Teaching assistants
## 308           Novotni (1985) 1985 37133954                     Peer tutoring
## 309             Nunes (2018) 2018 38296657               Small group tuition
## 310             Nunes (2018) 2018 38296657               Teaching assistants
## 311           Oakland (1975) 1975 37093585                     Peer tutoring
## 312             Olson (1990) 1990 37092590                          Feedback
## 313              Oner (1977) 1977 37092703                          Feedback
## 314          Onyehalu (1983) 1983 37092704                          Feedback
## 315     Osguthorpe (1986) PT 1986 40294937                     Peer tutoring
## 316              Pace (1986) 1986 38111450       Oral language interventions
## 317          Paquette (2003) 2003 37133956                     Peer tutoring
## 318      Paquette (2009) 1_1 2009 37092591                          Feedback
## 319      Paquette (2009) 1_1 2009 37092591                     Peer tutoring
## 320      Paquette (2009) 1_2 2009 40294939                     Peer tutoring
## 321      Paquette (2009) 1_2 2009 40294939                          Feedback
## 322            Parham (1993) 1993 37133957                     Peer tutoring
## 323             Patel (2017) 2017 38296659               Teaching assistants
## 324             Patel (2017) 2017 38296659                One to one tuition
## 325             Peeck (1979) 1979 37061141                          Feedback
## 326         Peeck (1985) 1_1 1985 37061139                          Feedback
## 327         Peeck (1985) 1_2 1985 40294942                          Feedback
## 328           Perkins (1988) 1988 37092708                          Feedback
## 329      Peterson (1979) SGT 1979 40294947               Small group tuition
## 330            Phelps (1989) 1989 37093590                     Peer tutoring
## 331       Philippakos (2012) 2012 37092592                          Feedback
## 332          Phillips (1990) 1990 38111314       Oral language interventions
## 333            Piercy (1997) 1997 38111403       Oral language interventions
## 334           Pinnell (1994) 1994 38878269               Small group tuition
## 335  Pollard-Durodola (2011) 2011 38111685       Oral language interventions
## 336            Prater (1993) 1993 37092593                          Feedback
## 337           Puhalla (2005) 2005 38111452       Oral language interventions
## 338            Rainey (1968) 1968 38111518       Oral language interventions
## 339   Ransford-Kaldon (2010) 2010 38878270               Small group tuition
## 340          Rashotte (2001) 2001 38878271               Small group tuition
## 341          Ratcliff (2009) 2009 37671611               Teaching assistants
## 342              Reid (1988) 1988 37092715                          Feedback
## 343           Reutzel (1994) 1994 38111657       Oral language interventions
## 344          Reynolds (1988) 1988 37092594                          Feedback
## 345       Reznitskaya (2001) 2001 38111589       Oral language interventions
## 346        Reznitskya (2002) 2002 38111590       Oral language interventions
## 347          Ribowsky (1985) 1985 38111618       Oral language interventions
## 348          Rickards (1978) 1978 37092778                          Feedback
## 349            Rienzo (2016) 2016 38296661                          Feedback
## 350           Roberts (2010) 2010 37671612               Teaching assistants
## 351           Rolfhus (2012) 2012 38878272               Small group tuition
## 352         Rosenthal (2006) 2006 37092595                          Feedback
## 353         Roskos (2011) OL 2011 40294950       Oral language interventions
## 354        Roussey (1992) FB 1992 40294951                          Feedback
## 355               Roy (2019) 2019 40398944                One to one tuition
## 356               Roy (2019) 2019 40398944                           Phonics
## 357               Roy (2019) 2019 40398944               Teaching assistants
## 358              Rust (1977) 1977 37092719                          Feedback
## 359              Rutt (2014) 2014 38296668               Teaching assistants
## 360              Rutt (2014) 2014 38296668                One to one tuition
## 361              Rutt (2015) 2015 38296667               Teaching assistants
## 362              Rutt (2015) 2015 38296667                           Phonics
## 363              Rutt (2015) 2015 38296667                One to one tuition
## 364             Sable (1987) 1987 38111591       Oral language interventions
## 365         Sanderson (1992) 1992 37133962                     Peer tutoring
## 366          Saunders (1999) 1999 38111594       Oral language interventions
## 367            Schetz (1994) 1994 38111519       Oral language interventions
## 368            Schunk (1993) 1993 37092597                          Feedback
## 369        Schunk (1993) 1_1 1993 37092598                          Feedback
## 370        Schunk (1993) 1_2 1993 43090192                          Feedback
## 371    Scruggs (1986) PT 1_1 1986 40294954                     Peer tutoring
## 372    Scruggs (1986) PT 1_2 1986 40294955                     Peer tutoring
## 373               See (2018) 2018 38296671               Teaching assistants
## 374               See (2018) 2018 38296671                One to one tuition
## 375          Sénéchal (1997) 1997 38111520       Oral language interventions
## 376          Sharpley (1983) 1983 37093595                     Peer tutoring
## 377            Sheard (2015) 2015 38296672               Small group tuition
## 378            Sheard (2015) 2015 38296672                           Phonics
## 379            Sheard (2015) 2015 38296672               Teaching assistants
## 380        Shisler (1986) PT 1986 43090193                     Peer tutoring
## 381           Sibieta (2016) 2016 37671584               Teaching assistants
## 382           Sibieta (2016) 2016 37671585               Teaching assistants
## 383           Sibieta (2016) 2016 38296673               Teaching assistants
## 384           Sibieta (2016) 2016 38296673                One to one tuition
## 385           Sibieta (2016) 2016 38296675       Oral language interventions
## 386          Siddiqui (2014) 2014 38296677                          Feedback
## 387           Siemens (2001) 2001 37133964                     Peer tutoring
## 388           Simmons (1995) 1995 37093596                     Peer tutoring
## 389             Simon (2004) 2003 38111672       Oral language interventions
## 390          Sindelar (1982) 1982 38878122               Small group tuition
## 391             Singh (1981) 1981 37093365                     Peer tutoring
## 392             Smith (2010) 2010 37133968                     Peer tutoring
## 393             Smith (2010) 2010 37133968                Digital technology
## 394      Sonnenschein (1986) 1986 37092727                          Feedback
## 395        Speckesser (2018) 2018 38296682                          Feedback
## 396            Spörer (2009) 2009 37116236                     Peer tutoring
## 397         Stainback (1972) 1972 37093602                     Peer tutoring
## 398          Stauffer (1966) 1966 38111621       Oral language interventions
## 399          Stauffer (1976) 1976 38111620       Oral language interventions
## 400             Stein (2008) 2008 37116233                     Peer tutoring
## 401          Stephens (2002) 2002 37133971                     Peer tutoring
## 402           Stevens (1987) 1987 37093603                     Peer tutoring
## 403            Styles (2014) 2014 38296685             Extending school time
## 404            Styles (2014) 2014 38296685               Small group tuition
## 405            Styles (2015) 2015 37671586               Teaching assistants
## 406        Sutherland (1999) 1999 37093606                     Peer tutoring
## 407             Swain (2010) 2010 37671517               Teaching assistants
## 408           Swanson (1977) 1977 37092790                          Feedback
## 409           Swenson (1975) 1975 37093367                     Peer tutoring
## 410          Tait (1973) 1_1 1973 37061134                          Feedback
## 411          Tait (1973) 1_2 1973 40294957                          Feedback
## 412            Taylor (1986) 1986 38111625       Oral language interventions
## 413            Taylor (1997) 1997 37093607                     Peer tutoring
## 414            Taylor (2002) 2002 37133974                     Peer tutoring
## 415      Tenenbaum (1986) FB 1986 40294958                          Feedback
## 416            Thames (1986) 1986 38111458       Oral language interventions
## 417          Thurston (2016) 2016 38296687       Oral language interventions
## 418           Tierney (2005) 2005 37133976                     Peer tutoring
## 419            Tobias (1984) 1984 37061135                          Feedback
## 420             Tokar (1976) 1976 37092791                          Feedback
## 421            Tomita (2008) 2008 37092612                          Feedback
## 422            Top (1985) PT 1985 43090197                     Peer tutoring
## 423            Top (1987) PT 1987 43090198                     Peer tutoring
## 424           Topping (2004) 2004 37133980                     Peer tutoring
## 425           Topping (2004) 2004 37133982                     Peer tutoring
## 426           Topping (2011) 2011 37116207                     Peer tutoring
## 427         Torgerson (2014) 2014 38296693               Small group tuition
## 428         Torgerson (2018) 2018 38296689               Small group tuition
## 429          Torgesen (2006) 2006 38878260               Small group tuition
## 430          Torgesen (2010) 2010 38878273               Small group tuition
## 431            Tracey (2019) 2019 40398947               Small group tuition
## 432         Truesdale (1976) 1976 37093368                     Peer tutoring
## 433          Tuominen (2008) 2008 37092613                          Feedback
## 434             Tymms (1989) 1989 37133983                     Peer tutoring
## 435             Tymms (2011) 2011 37116208                     Peer tutoring
## 436            Vadasy (2006) 2006 37671592               Teaching assistants
## 437            Vadasy (2007) 2007 37671636               Teaching assistants
## 438            Vadasy (2008) 2008 37671638               Teaching assistants
## 439        Vadasy (2008) SGT 2008 40294961               Small group tuition
## 440         Vadasy (2008) TA 2008 37671637               Teaching assistants
## 441         Vadasy (2008) TA 2008 43090199               Teaching assistants
## 442            Vadasy (2009) 2009 37671588               Teaching assistants
## 443            Vadasy (2009) 2009 37671588               Small group tuition
## 444            Vadasy (2010) 2010 37671589               Teaching assistants
## 445            Vadasy (2013) 2013 37671614               Teaching assistants
## 446          Van Keer (2004) 2004 37133984                     Peer tutoring
## 447          Van Keer (2010) 2010 37116237                     Peer tutoring
## 448        van Kleeck (2006) 2006 38111552       Oral language interventions
## 449    van Oudenhoven (1987) 1987 37093609                     Peer tutoring
## 450 Van Oudenhoven (1987) FB 1987 40294962                          Feedback
## 451          VanEvera (2003) 2003 37092614                          Feedback
## 452          Vellella (1996) 1996 37092599                          Feedback
## 453        Wade-Stein (2004) 2004 37092600                          Feedback
## 454             Walsh (2006) 2006 38111527       Oral language interventions
## 455             Walsh (2009) 2009 38111686       Oral language interventions
## 456           Wang (2008) TA 2008 43090202               Teaching assistants
## 457             Wasik (2001) 2001 38111661       Oral language interventions
## 458             Wasik (2006) 2006 38111662       Oral language interventions
## 459             Welch (1995) 1995 37671616               Teaching assistants
## 460          Wentling (1973) 1973 37092796                          Feedback
## 461             White (2000) 2000 37133987                     Peer tutoring
## 462        Whitehurst (1994) 1994 38111668       Oral language interventions
## 463          Wiersema (1992) 1992 37093610                     Peer tutoring
## 464           Wiggins (2017) 2017 38296697                          Feedback
## 465           Wiggins (2017) 2017 38296697                Digital technology
## 466           William (2004) 2004 37092615                          Feedback
## 467              Wise (1992) 1992 37092601                          Feedback
## 468            Wixson (1986) 1986 38111460       Oral language interventions
## 469        Wolter (1975) 1_1 1975 37092602                          Feedback
## 470        Wolter (1975) 1_2 1975 40294963                          Feedback
## 471              Word (1990) 1990 37671591               Teaching assistants
## 472              Word (1990) 1990 37671591               Reducing class size
## 473              Wyne (1979) 1979 37092800                          Feedback
## 474              Yang (2016) 2016 37116218                     Peer tutoring
## 475            Yarrow (2001) 2001 37133992                     Peer tutoring
## 476           Yeazell (1982) 1982 38111597       Oral language interventions
## 477           Yeazell (1982) 1982 38111597 Metacognition and self-regulation
## 478               Yin (2005) 2005 37092616                          Feedback
## 479             Young (2000) 2000 37092603                          Feedback
## 480         Zimmerman (1977) 1977 37092801                          Feedback
```

```r
#write.csv(all,'/home/jon/json/batch1.csv', row.names=FALSE)
```

