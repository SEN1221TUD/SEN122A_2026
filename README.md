# SEN122A- Statistical Analysis of Choice Behaviour 2026

## 1. Introduction

Welcome to the _Choice behaviour modelling_ section of the SEN112A course repository. In this repository, you will find Jupyter notebooks for the lab sessions, [step-by-step instructions for setting up your Python environment](./Setting_up_environment/Settting_up_your_environment.md), and a discussion forum where you can ask questions related to the course content.

## 2. Course description

Mathematical models of choice behaviour –henceforth referred to as "Discrete Choice Models" (DCMs)– are widely used to study the decision-making behaviour of individuals across numerous domains, including transportation, marketing, and health. DCMs are used to infer preferences over attributes and alternatives and predict the impact of new policies.

This course aims to equip students in the socio-technical domain with a comprehensive understanding of DCMs. You will learn the theoretical underpinnings of choice models and gain practical hands-on experience in estimating and applying these models to solve real-world problems.

The course consists of oral lectures and lab sessions. During the lab sessions, students will work with Python-based tools to estimate models and analyze datasets. Attendance at both the lectures and lab sessions is highly recommended to keep up with the course content, although it is not mandatory.

Below, you can find the dates for the lab sessions and the practical exams:

| **Week** | **Event**                       | **Date**          | **Time**    | . _Remarks_                          |
| -------- | ------------------------------- | ----------------- | ----------- | ------------------------------------ |
| 2.2      | Python environment support hour | November 16, 2026 | 09:45-10:45 | _optional_ Flux Hall D               |
| 2.2      | Lab session 1 (MNL)             | November 16, 2026 | 10:45-12:30 |                                      |
| 2.3      | Lab session 2 (MXL)             | November 23, 2026 | 10:45-12:30 |                                      |
| 2.4      | Lab session 3 (ML)              | November 30, 2026 | 10:45-12:30 |                                      |
| 2.4      | Q&A session                     | December 04, 2026 | 13:45-15:45 | Student can ask questions            |
| 2.5      | **Practical Exam**              | December 07, 2026 | 13:30-15:30 |                                      |
| 2.6      | Exam review session.            | December 16, 2026 | 12:45-13:30 | No other opportunity will be offered, IDE-Computer Room Shift |
| 2.8      | Resit **Practical Exam**            | January 15, 2027  | 13:30-15:30 |                                      |
| 2.9      | Resit exam review session       | January 22, 2027  | 12:45-13:30 | No other opportunity will be offered, CEG-Computer Room 0.070 |
| 2.10     | Q&A exam preparation Part 1     | January 25, 2027  | 15:45-16:45 |                                      |
| 2.10     | Theoretical exam                | January 28, 2027  | 09:00-12:00 |                                      |
| 3.9      | Resit theoretical Exam          | April 08, 2027    | 13:30-16:30 |                                      |
| 3.10     | Exam review session             | April 15, 2027    | 13:30-15:30 | No other opportunity will be offered |

Note: in case of descripancies between the dates in this table and the official TU Delft schedule, the official TU Delft schedule takes precedence.

Please review the information below carefully.

## 3. Lab sessions

### 3.1. Overview of lab sessions

Lab sessions are offered in the form of Jupyter notebooks and aim to demonstrate and reinforce knowledge about discrete choice models, the underlying assumptions, estimation techniques, and how to interpret outcomes. They provide **hands-on** experience in discrete choice modelling, which is essential to master the method. Each lab session comprises three parts: A, B and C, and include a series of **exercises**. Lab sessions A and B contain guidance and instructions to help you conduct the work and complete the exercises, while lab session C requires you to apply your knowledge **independently** (i.e. without direct guidance/instructions).

`Lab session 1` introduces discrete choice models, focusing specifically on the Multinomial Logit (MNL) model based on random utility theory. You will acquire skills to explore choice datasets, build and estimate choice models using specialised Python package called Biogeme, and perform statistical tests to compare different model specifications.

`Lab session 2` focuses on the Mixed Logit models. You will gain proficiency in building and estimating various types of Mixed Logit models by altering assumptions about unobserved preference and taste heterogeneity. Furthermore, you will explore the impact of the number of draws on the estimation outcomes.

`Lab session 3` focuses on the latest developments in the field: combining discrete choice modelling and machine learning for choice behaviour analysis. You will work with neural networks and explore how they can be integrated within utility-based choice models.

For the lab sessions, we use Python notebooks (aka Jupyter Notebooks). You can set up the required Python environment in one of two ways:

- using Anaconda
- using Pip

**Instructions** for both options are given [here](./Setting_up_environment/Settting_up_your_environment.md).

If you are **unfamiliar with Python**, we recommend completing [**lab session 0**](./Lab_sessions/Lab_session_00/lab_session_00.ipynb) before starting with theother ab sessions. It introduces the Python skills required for the lab sessions, including working with data structures, utilising external libraries, exploring data, and creating visualisations.

### 3.2. Lab session publication dates

The lab sessions and **answers** will be made available on the following dates:

| Week | Lab session | Publication date<br>Lab session | Publication date<br>Answers |
| :--: | :---------: | :-----------------------------: | :-------------------------: |
|  47  |    Lab 1    |       ⏳ 09-11-2026 09:00       |     ⏳ 23-11-2026 09:00     |
|  48  |    Lab 2    |       ⏳ 23-11-2026 09:00       |     ⏳ 30-11-2026 09:00     |
|  49  |    Lab 3    |       ⏳ 30-11-2026 09:00       |     ⏳ 03-12-2026 09:00     |

## 4. Tutorials

The [tutorials](https://github.com/SEN1221TUD/Tutorials) are supplementary course materials designed to deepen your understanding of key concepts in choice modelling. Although they do not contain exercises, they form part of the SEN122A course material and support the topics covered in the lecturers ad lab sessions.<br>

The following tutorials are currently available:<br>

[Tutorial 1](https://github.com/SEN1221TUD/Tutorials/blob/main/tutorial1/tutorial1_DGP_and_bias.ipynb): The data generating process and bias <br>
[Tutorial 2](https://github.com/SEN1221TUD/Tutorials/blob/main/tutorial2/tutorial2_The_loglikelihood_function.ipynb): The loglikelihood function<br>
[Tutorial 3](https://github.com/SEN1221TUD/Tutorials/blob/main/tutorial3/tutorial3_concave_likelihood_MNL.ipynb): The concave likelihood function of the linear-additive RUM-MNL model<br>
[Tutorial 4](https://github.com/SEN1221TUD/Tutorials/blob/main/tutorial4/tutorial4_Local_vs_global_maxima.ipynb): Local versus global maxima<br>
[Tutorial 5](https://github.com/SEN1221TUD/Tutorials/blob/main/tutorial5/tutorial5_Ignoring_panel_structure.ipynb): The impact of ignoring the panel structure of choice data<br>
[Tutorial 6](https://github.com/SEN1221TUD/Tutorials/blob/main/tutorial6/tutorial6_Expected_max_utility.ipynb): The expected maximum utility and the LogSum formula<br>

Additional tutorials may be added during the course.

## 5. Q&A forum

We use the [Issues](https://github.com/SEN1221TUD/SEN122A_2026/issues) section as the Q&A forum for Part 1: Choice Behaviour Modelling. You can use it to ask questions related to lecture content, lab sessions, or technical issues with Python. <br>

Before you create a new issue, please check whether another student has already asked the same question. If so, you can also contribute to ongoing discussions by adding a comment or providing additional insights. As an example, we have already created the first issue; see [Issues](https://github.com/SEN1221TUD/SEN122A_2026/issues).

To create a new issue (question or problem), follow these steps:

1. Go to the [Issues](https://github.com/SEN1221TUD/SEN122A_2026/issues) section of the course repository.
2. Click the green "New issue" button in the upper-right corner of your screen.
3. Enter an informative title for your issue (e.g., "logit model of BIOGEME does not import in my notebook").
4. Describe your issue clearly and concisely. If you are reporting a technical problem, include the error message.
5. Choose an appropiate topic label (e.g., if the question is about lab session 1, choose label "lab session 1") by clicking on the gear icon next to "Labels".
6. Click on "Submit new issue" in the green button below the text description.

After that, the lecturer or teaching assistant will reply to your question. Also, you are encouraged to reply to questions posted by your fellow students! If you know how to help your fellow student with an issue, share your thoughts!
