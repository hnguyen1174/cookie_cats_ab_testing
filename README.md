## AB Testing for Cookie Cats, a Mobile Game

Cookie Cats is a popular mobile puzzle game developed by [Tactile Games](https://tactilegames.com/). This is a classic game where you need to connect three pieces of puzzle of the same type to clear the board and score points.

### Description

As players move to higher level, they will see gates that ask them to either wait for a period of time, or make an in-app purchase to progress. In this project, I am interested in performing an A/B test to understand the effect of moving the first gate from level 30 to level 40 on player retention.

### The Data

The dataset contains 90,189 players that installed the game while the A/B test took place. The features are as follows:

* `userid`: player unique identification
* `version`: whether the player is placed in the control group (`gate_30`; the first gate is placed at level 30) or the test group (`gate_40`; the first gate is placed at level 40).
* `sum_gamerounds`: the number of game rounds played by the player during the **first week** after installation
* `retention_1`: 1-day retention of player after installation
* `retention_7`: 7-day retention of player after installation

### A/B Testing Process:

1. Understanding business problem and the data
2. Form a hypothesis and check assumptions
3. Build a randomization strategy
4. Set metrics
5. Choose a sample size
6. Collect the data
7. Perform exploratory data analysis and process data
8. Check normality and homogeneity
9. Apply tests (Shapiro, Levene Test, T-Test, Welch Test, Mann Whitney U Test)
10. Evaluate the results on the metrics
11. Make inferences
12. Make recommendations