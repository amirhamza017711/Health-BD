# Bangladesh's Transition from ICD-10 to ICD-11: A Journey Towards Modernized Health Coding

## Introduction

In late 2023, Bangladesh started the journey of transitioning from ICD-10 to ICD-11, aiming to modernize its health information system and improve disease classification and reporting. As part of this transition, a pilot phase was initiated in six hospitals, employing two different approaches for ICD-11 integration based on the existing digital infrastructure.

## The Pilot Phase: Implementing ICD-11 in Six Hospitals

To assess the feasibility and effectiveness of ICD-11, six hospitals were selected for piloting, categorized based on their health information systems:

### 1. OpenMRS-Based Hospitals (WHO ICD-11 API Integration)

Three district hospitals leveraged OpenMRS, integrated with the WHO ICD-11 API to facilitate morbidity (OPD, emergency) and mortality (MCCoD) coding. The hospitals included:

- **Cumilla District Hospital**
- **Nilphamari District Hospital**
- **Barguna District Hospital**

This integration enabled structured coding of patient diagnoses and causes of death.

### 2. DHIS2-Based Hospitals (ICD-11 Codes in Dropdowns)

Three other hospitals incorporated ICD-11 into the existing DHIS2 platform by manually adding ICD-11 codes into dropdown menus. These hospitals were:

- **Cox’s Bazar District Hospital**
- **Khulna Medical College Hospital**
- **Rajshahi Medical College Hospital**

Bangladesh initially planned for an integrated morbidity and mortality tracker within DHIS2. While WHO had already developed a customized ICD-11 application for MCCOD (Medical Certification of Cause of Death), there was no equivalent app available for morbidity coding at the time of piloting. As a result, ICD-11 morbidity and mortality coding had to be manually incorporated using dropdown menus. Bangladesh continued using this approach to maintain consistency while simultaneously requesting WHO to develop a customized morbidity app to enable full ICD-11 integration within DHIS2.

## Challenges Encountered During the Pilot Phase

### 1. Challenges in OpenMRS Implementation

- **Limited Scope of ICD-11 Usage:** The inpatient module of OpenMRS is still under development. Consequently, ICD-11 could only be utilized in outpatient departments (OPD), emergency departments, and for MCCOD.
- **Data Remains Locally Stored:** The lack of centralized synchronization meant that hospitals using OpenMRS continued entering routine health information into DHIS2, leading to a double workload.
- **Limited Use of Postcoordination:** Findings from the pilot phase indicated very little usage of postcoordination in OpenMRS-based piloting areas, suggesting the need for further training and system improvements.
- **Initial Absence of Foundation URI Storage:** Initially, only ICD-11 codes were stored, without keeping the `foundationUri`. Later, it was realized that storing `foundationUri` is essential for usability and data analysis. As a result, this functionality was added to the backend.

### 2. Challenges in DHIS2 Implementation

- **Dropdown Limitations:** Since DHIS2 lacked a built-in API connection for ICD-11, the dropdown approach was used. However, ICD-11 is not designed to function as a dropdown-based classification, making data entry cumbersome and inefficient.
- **Dual Data Entry Burden:** As Bangladesh’s national health statistics are still produced using ICD-10, hospitals using ICD-11 in DHIS2 were also required to enter the same data in ICD-10. This double data entry requirement led to frustration among healthcare workers, resulting in low motivation to input ICD-11 data.
- **Future System Constraints:** Given that ICD-11 was not intended to be used as dropdown selections, it became evident that long-term implementation should focus on full-fledged hospital automation rather than manual input into DHIS2.

### 3. Inconsistent MCCOD Data Entry

In Bangladesh, routine health information system (HIS) data is formulated by a statistician, while MCCOD data entry is performed by a nurse from the inpatient department. Regardless of the HIS platform (OpenMRS or DHIS2), nurses had to enter the same data twice. This redundancy led to minimal data entry for MCCOD. However, OPD and emergency departments performed well because physicians use the automation system in real time, eliminating redundant data entry and additional workload for them.

## Lessons Learned and Next Steps

The pilot phase provided crucial insights into the strengths and limitations of ICD-11 integration in Bangladesh’s healthcare system. The key takeaways shaped the country’s next phase of implementation.

### 1. Establishing a Central Terminology Registry

Bangladesh is in the process of formulating a **Central Terminology Registry**, which will adopt ICD-11 for coding symptoms, signs, diagnoses, and medications. This initiative paves the way for nationwide expansion of ICD-11 implementation in hospitals equipped with automation systems.

#### Why ICD-11 for the Terminology Registry?

- **Free of Cost** – No licensing fees are required, making it a cost-effective solution.
- **Global Community Support** – ICD-11 is backed by a robust global community, ensuring continuous updates and improvements.
- **Ready Technology** – WHO has provided APIs and tools that facilitate seamless integration with existing health information systems.

### 2. Switching to Localized ICD-11 Deployment

Initially, ICD-11 was deployed using the WHO ICD-11 API. However, Bangladesh is now transitioning to a **localized Docker container deployment**. This shift significantly reduces dependency on internet connectivity, ensuring a more stable and efficient system for hospitals, especially in remote areas.

### 3. Scaling Up ICD-11 to 150 Hospitals

Building on the lessons from the pilot phase, Bangladesh plans to **expand ICD-11 implementation to 150 hospitals** that have hospital automation systems. This expansion will facilitate the integration of ICD-11 data directly into a central shareable health record repository, eliminating the need for duplicate data entry into DHIS2.

### 4. Future of DHIS2 and ICD-11 Integration

- **MCCOD Application Adoption:** In DHIS2, the WHO MCCOD app with ICD-11 API will be adopted for mortality coding.
- **Exploring Custom Morbidity Apps:** If a customized app for morbidity coding with ICD-11 API becomes available, Bangladesh will integrate it into DHIS2. Otherwise, ICD-10 will continue to be used for morbidity coding, but a **mapping system** will be developed to transition ICD-10 data into ICD-11 over time.

### 5. Capacity Building for ICD-11 Data Analysis

Bangladesh recognizes the need for **capacity building** in analyzing data coded with ICD-11. Training healthcare professionals and statisticians in **interpreting and utilizing ICD-11-coded data** effectively will be essential for decision-making and policy development.

### 6. Gradual Phase-Out of DHIS2 for Hospital-Based Coding

Over time, as hospital automation systems expand, **ICD-11 data will be directly recorded in these systems**. DHIS2 will gradually be phased out for individual patient coding but will continue to serve **program-specific purposes and aggregate data collection** at the national level.

## Conclusion

Bangladesh’s transition from ICD-10 to ICD-11 represents a **significant leap** in modernizing the country’s health information system. While the pilot phase revealed implementation challenges, it also provided a roadmap for future scaling. By addressing **data synchronization issues, reducing dependency on internet-based APIs, eliminating redundant data entry, and strengthening capacity building** for ICD-11 data analysis, Bangladesh aims to **enhance healthcare coding efficiency, improve statistical accuracy, and align with global health standards** for morbidity and mortality reporting.

