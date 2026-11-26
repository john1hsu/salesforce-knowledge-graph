---
id: kt:computer-science
type: ExternalConcept
title: Computer Science
aliases: [computing science, computing as a discipline, CS discipline]
domain: platform-architecture
summary: >-
  The study of computers and computing, from the theory of what can be computed and the design of algorithms to
  hardware, software, networks and their uses; it is the parent discipline of distributed computing, cloud
  computing and the programming-language, database and security ideas the Salesforce Platform is built from.
release: "Winter '27"
status: concept
broader: [kt:science]
related: [kt:cloud-computing, kt:apex, kt:soql, kt:data-management, kt:generative-ai]
relations:
  - {predicate: hasPart, object: kt:distributed-computing}
  - {predicate: hasPart, object: kt:software-engineering}
sources:
  - id: s1
    title: "Computer science"
    publisher: Encyclopaedia Britannica (Geneva G. Belford, Allen Tucker)
    url: https://www.britannica.com/science/computer-science
    type: textbook
    accessed: 2026-11-26
  - id: s2
    title: "Computing as a Discipline (Final Report of the ACM Task Force on the Core of Computer Science)"
    publisher: Communications of the ACM 32(1), Peter J. Denning et al.
    url: https://www.cs.auckland.ac.nz/courses/compsci747s2c/lectures/denning-1989.pdf
    type: peer-reviewed
    accessed: 2026-11-26
  - id: s3
    title: "On Computable Numbers, with an Application to the Entscheidungsproblem"
    publisher: A. M. Turing (1936), hosted by the University of Virginia
    url: https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf
    type: peer-reviewed
    accessed: 2026-11-26
  - id: s4
    title: "ACM, IEEE-CS, and AAAI Release CS2023 Curricular Guidelines"
    publisher: Association for Computing Machinery
    url: https://www.acm.org/articles/bulletins/2024/june/cs2023-curricular-guidelines
    type: academic
    accessed: 2026-11-26
created: 2026-11-26
---

# Computer Science

Computer science is, in Britannica's words, "the study of computers and computing," including the theoretical and algorithmic foundations beneath them, the hardware and software that realise them, and the ways they are used to process information.[^s1] The ACM Task Force on the Core of Computer Science gave a sharper working definition in 1989: the systematic study of algorithmic processes that describe and transform information, covering their theory, analysis, design, efficiency, implementation and application.[^s2] For a Salesforce architect, it is the vocabulary behind every platform decision, from why a query needs a selective index to why an event bus delivers messages eventually rather than instantly.[^s1][^s2]

## Origins

The discipline grew out of mathematics, electrical engineering, physics and management information systems. Mathematics contributed binary representation and the stored-program idea, while electrical engineering contributed circuit design based on Boolean algebra.[^s1] Its theoretical starting point is usually traced to Alan Turing's 1936 paper "On Computable Numbers," which defined computable numbers as real numbers whose decimal expansions can be calculated by finite means and modelled calculation as an automatic machine reading and writing symbols on a tape under a finite set of configurations.[^s3] Turing described a universal machine able to simulate any other such machine, and showed that no general procedure can decide whether an arbitrary machine behaves in a certain way, which led him to conclude that Hilbert's decision problem (the Entscheidungsproblem) has no solution.[^s3] Britannica pairs Turing's machine with John von Neumann's stored-program concept as the field's twin origins, and dates computer science's emergence as an independent academic discipline to the early 1960s, after the first high-level languages such as FORTRAN and COBOL in the 1950s.[^s1]

## Structure of the field

The 1989 ACM report argued that computing intertwines three paradigms, each with its own roots: **theory** (from mathematics), **abstraction or modelling** (from the experimental scientific method) and **design** (from engineering).[^s2] It divided the discipline into nine subareas: algorithms and data structures; programming languages; architecture; numerical and symbolic computation; operating systems; software methodology and engineering; database and information retrieval systems; artificial intelligence and robotics; and human-computer communication.[^s2]

Modern descriptions are broader. Britannica lists fifteen fields, adding among others networking and communication, parallel and distributed computing, security and information assurance, graphics and visual computing, platform-based development, and social and professional issues.[^s1] The curriculum community keeps that map current: in CS2023, the ACM, the IEEE Computer Society and the Association for the Advancement of Artificial Intelligence jointly published guidelines on the knowledge and competencies an undergraduate computer science degree should build, drafted by a 17-member international steering committee after surveying hundreds of academics and industry practitioners.[^s4] The inclusion of AAAI as a co-publisher reflects how central artificial intelligence has become to the core of the field.[^s4]

## Why it matters on the Salesforce Platform

Each subarea named by the ACM task force has a direct counterpart in daily Salesforce work. Algorithms and data structures decide whether Apex code that loops over collections stays inside CPU and heap limits; programming-language theory underpins Apex and the declarative languages of formulas and flows; and database and information retrieval systems explain how SOQL queries are planned and why selectivity matters.[^s2] Operating-systems and architecture ideas such as resource isolation and scheduling reappear in a multitenant platform that must share hardware fairly among tenants, and the parallel and distributed computing field named by Britannica is the basis of cloud infrastructure.[^s1][^s2] Artificial intelligence, once one subarea among nine, now drives generative features and agents across the platform.[^s2][^s4]

## Connections

Computer science is the parent discipline of **distributed computing**, which Britannica lists as one of its fields (parallel and distributed computing), and of **software engineering**, which the ACM task force named as a core subarea.[^s1][^s2] **Cloud computing** applies the field's networking, distributed-systems and operating-systems ideas as a delivery model.[^s1] **Apex** and **SOQL** are applications of its programming-language and database subareas, and **data management** draws on the information-management field Britannica describes.[^s1][^s2] **Generative AI** belongs to the artificial-intelligence strand that both the 1989 report and the AAAI-backed CS2023 guidelines treat as part of the discipline's core.[^s2][^s4] Its broader context is **science**, under which Britannica classifies it while noting its engineering roots.[^s1]

## Sources

[^s1]: Encyclopaedia Britannica, "Computer science" (Geneva G. Belford, Allen Tucker). https://www.britannica.com/science/computer-science (accessed 2026-11-26)
[^s2]: Peter J. Denning, Douglas E. Comer, David Gries, Michael C. Mulder, Allen Tucker, A. Joe Turner and Paul R. Young, "Computing as a Discipline", Communications of the ACM 32(1), January 1989. https://www.cs.auckland.ac.nz/courses/compsci747s2c/lectures/denning-1989.pdf (accessed 2026-11-26)
[^s3]: A. M. Turing, "On Computable Numbers, with an Application to the Entscheidungsproblem" (1936). https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf (accessed 2026-11-26)
[^s4]: Association for Computing Machinery, "ACM, IEEE-CS, and AAAI Release CS2023 Curricular Guidelines". https://www.acm.org/articles/bulletins/2024/june/cs2023-curricular-guidelines (accessed 2026-11-26)
