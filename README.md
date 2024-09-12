# Voting_Project

This repository implements different voting methods to determine the winner of an election. The project includes several classes, each representing a unique voting algorithm.

**Classes Overview**

Majority: Determines the winner based on the majority voting method, where a candidate must receive more than 50% of the votes.

InstantRunOff: Extends the majority method by using the Instant Runoff process, eliminating the candidate with the fewest votes in each round until a majority winner is found.

Condorcet: Implements the Condorcet method, which determines the winner as the candidate who would win a head-to-head comparison against every other candidate.

Borda: Uses the Borda Count method, where candidates are ranked, and points are assigned based on their position. The candidate with the highest total points wins.

**Voting Data**

The voting data is stored in a file, which contains lists of votes for each candidate. The classes use this data to determine the winner according to their specific method.

**Tests**

Test cases are available for all classes to ensure correctness and validate their functionality with the provided voting data.
