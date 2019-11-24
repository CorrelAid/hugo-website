---
title:      "Hackathon with GLEIF"
date:       2019-11-27T00:00:00+02:00
image:      "gleif-hackathon.jpg"
summary:    "Visualizing Relationships between Legal Entities"
draft:      false
categories:       
    - Veranstaltungen
    - Hackathon
    - Projekt
author: 
    name:           "CorrelAid"
    image:          "correlaid.jpg"
    description:    "CorrelAid ist seit Juli 2015 als gemeinnütziger Verein in Konstanz eingetragen. Wir haben derzeit ein ehrenamtliches Organisationsteam aus 15 Leuten und ein Netzwerk von 650 ehrenamtlichen DatenanalystInnen. Wir haben bereits über 10 Volunteering-Projekte mit kleinen und großen NPOs (u.a. Ashoka, europäisches Jugendparlament, streetfootballworld) initiert, über 50 Workshops für DatenanalystInnen durchgeführt, und zahlreiche Vorträge (u.a. bei Die Zeit, NPO-Tag von Microsoft, Bayreuther Dialoge) gehalten."
    twitter:        "https://twitter.com/correlaid"
    facebook:       "https://facebook.com/WeAreCorrelAid"
    github:         "https://github.com/correlaid"
    email:          "kontakt@correlaid.org"
    website:        "https://correlaid.org"
meta:
    title:          "CorrelAid - CorrelAidX - Kick-off für unsere Data-for-Good-Lokalgruppen"
    description:    "CorrelAid ist ein dezentrales Projekt. Jeder und jede, die ihre Coding- und Statistik-Kenntnisse für den guten Zweck einsetzen will, soll bei uns dazu die Möglichkeit haben."
    image:          "509-correlaidx_2.jpg"
    keywords:       "CorrelAid, Data4Good, CorrelAidX, LC, local chapter, Lokalgruppen"
---

On 18th and 19th July CorrelAid and Global Legal Entity Identifier Fondation (GLEIF) organized a joint hackathon on visualization of legal entity relationship data. GLEIF is a supra-national not-for-profit organization established by the Financial Stability Board in June 2014 tasked to support the implementation and use of the Legal Entity Identifier (LEI). The LEI is a 20-character, alpha-numeric code based on the ISO 17442 standard developed by the International Organization for Standardization (ISO). It connects to key reference information that enables clear and unique identification of legal entities participating in financial transactions. Each LEI contains information about an entity’s ownership structure and thus answers the questions of 'who is who’ and ‘who owns whom’. Simply put, the publicly available LEI data pool can be regarded as a global directory, which greatly enhances transparency in the global marketplace. GLEIF offers all available data on legal entities and corresponding relationships in a cleaned and structured format. The so-called Golden Copies are updated three times a day and are available for free. Furthermore, everybody can download the files without any registration or login process. 


{{< image 
    image="gleif-1.jpg"
>}}
GLEIF 1
{{< /image >}}

Together with team members of GLEIF, our team - consisting of Frie, Maira, Chris and Jan - developed an interactive visualization tool to display ownership structures of legal entities with registered LEIs. The tool can be used to easily and intuitively explore ownership structures on the one hand and to identify existing contradictions in the declared networks. GLEIF makes available a challenge facility, which extends the ability to trigger updates of a LEI record to all interested parties. Specifically, it offers easy and convenient means to trigger the verification and, where required, speedy update of LEI records including related reference data.

{{< image 
    image="gleif-2.jpg"
>}}
GLEIF 2
{{< /image >}}

We decided to use a combination of a JavaScript Frontend and a Python Backend to develop a modern web application. For the backend part we utilized the packages networkx and fastapi. The data structures including nodes and edges called for graph library such as networkx. Fastapi helped us to rapidly develop a minimal REST API to deliver queried graphs to the frontend. The frontend part was realised using Vue.js. Vis.js was used to transform the nodes and edges into feasible, interactive network graphs. The final application was deployed using a setup of docker and nginx.

{{< image 
    image="gleif-3.jpg"
>}}
GLEIF 3
{{< /image >}}

During the two days, we were able to finish a basic prototype which enables users to search for a legal entity (using the API developed by GLEIF to access the data) and to find all ownership structures related to this entity. The recent weeks were used for fine-tuning and to implement some edge-cases. The code of the application is available at [https://github.com/CorrelAid/gleif-level2-client/](https://github.com/CorrelAid/gleif-level2-client/) under an Open Source license.

All of us learned a lot during the project. We like to thank our project partner GLEIF for the friendly environment, the fine food, and the opportunity to work on an interesting and sustainable project.

