# Why Knowledge Graphs

## Word Salad

An `ontology` in this space is

> the schema that defines the relationships between objects in a graph and the relationships of those relationships.

i.e. We can define that a "sibling" relationship from `A` to `B` and a "parent" relationship from `B` to `C`
defines an "aunt/uncle" relationship.
We would not need to define a separate relationship from `A` to `C` for how these two people connect;
it is defined it on the relationships themselves.

## Complications with Releasable Data

Something as apparently simple as

> give me all the releasable lexicals on a concept,

involves `concept join...join...join...join`.

Something more complicated, like

> give me all the HCC codes mapped to all parent ICD-10 codes of the primary ICD-10 code of an IMO lexical

involves `split_part(icd10cm_hcc_model_cat, ';', 1)`

One-to-many relationships stored as a delimited string in a single database column.

## Complications with Medication

In the Medication space, we are working with two code systems: call them X and Y.
Our users wanted to provide a code in X and get all related codes in Y, and vice-versa.
Our internal teams required that an IMO lexical be in the middle.
Our content is not in a state where a single IMO lexical is mapped to both code systems X and Y.

- Code system X has one set of lexicals
- Code system Y has another set of lexicals
- There is no intersection

As such, we had to create these relationships ourselves. This looks like [Master Search Data Medication](./Diagrams/MsdMedication.drawio.png).

It's a brutal combination of rules to make these relationships work, and some of them we made up.

Why?

The provided data structures.
It is overly complicated to provide releasable medication data to customers.

Think about one part: Given a user's NDC code, we need to

1. find the related RxNorm codes
1. find a lexical mapped to it.
   - So, we go from NDC to IMO to... RxNorm directly?
1. But then we need IMO codes for those RxNorm.
   - So we get the IMO codes mapped to RxNorm?
   - But those are different than the ones mapped to NDC
   - Do we go back to NDC?
   - Do we get more NDC codes based on the NDC code we started with?
   - Is our data literally running in circles?
