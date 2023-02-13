import streamlit as st

def result(align1,align2,sc):
  st.write("Aligned Sequence 1:", align1)
  st.write("Aligned Sequence 2:", align2)
  st.write('Score =',sc)

def needleman_wunsch(seq_1, seq_2):
  m, n = len(seq_1), len(seq_2)
  dp = [[0] * (n + 1) for _ in range(m + 1)]

  # Initialize the first row and first column
  for i in range(1, m + 1):
    dp[i][0] = dp[i - 1][0] + (-2)
  for j in range(1, n + 1):
    dp[0][j] = dp[0][j - 1] + (-2)  

    # Fill in the DP matrix
  for i in range(1, m + 1):
    for j in range(1, n + 1):
      match = dp[i - 1][j - 1] + (2 if seq_1[i - 1] == seq_2[j - 1] else -2)
      mis_match = dp[i - 1][j] + (-2)
      gap = dp[i][j - 1] + (-2)
      dp[i][j] = max(match, mis_match, gap)

  score = dp[m][n]
  sc=score

  # Traceback to find the optimal alignment
  align1, align2 = '', ''
  i, j = m, n
  while i > 0 and j > 0:
    score = dp[i][j]
    diag_score = dp[i - 1][j - 1]
    up_score = dp[i][j - 1]
    left_score = dp[i - 1][j]
    if score == diag_score + (2 if seq_1[i - 1] == seq_2[j - 1] else -2):
      align1 = seq_1[i - 1] + align1
      align2 = seq_2[j - 1] + align2
      i -= 1
      j -= 1
    elif score == left_score - 2:
      align1 = seq_1[i - 1] + align1
      align2 = '-' + align2
      i -= 1
    else:
      align1 = '-' + align1
      align2 = seq_2[j - 1] + align2
      j -= 1

  # Add remaining gaps if any
  while i > 0:
    align1 = seq_1[i - 1] + align1
    align2 = '-' + align2
    i -= 1
  while j > 0:
    align1 = '-' + align1
    align2 = seq_2[j - 1] + align2
    j -= 1

  result(align1, align2, sc)
  return None

def smith_waterman(seq1, seq2):
  m, n = len(seq1), len(seq2)
  dp = [[0] * (n + 1) for _ in range(m + 1)]
  # Initialize the first row and first column to zero
  for i in range(1, m + 1):
    dp[i][0] = 0
  for j in range(1, n + 1):
    dp[0][j] = 0
# Fill in the DP matrix
  for i in range(1, m + 1):
    for j in range(1, n + 1):
      match = dp[i - 1][j - 1] + (2 if seq1[i - 1] == seq2[j - 1] else -2)
      mismatch = dp[i - 1][j] + (-2)
      gap = dp[i][j - 1] + (-2)
      dp[i][j] = max(0, match, mismatch, gap)
      #print('Matrix',dp[i][j]) 

# Find the maximum score and its position
  max_score = 0
  max_i, max_j = 0, 0
  for i in range(1, m + 1):
    for j in range(1, n + 1):
      if dp[i][j] > max_score:
        max_score = dp[i][j]  
        max_i, max_j = i, j

  # Traceback to find the optimal alignment
  align1, align2 = '', ''
  score = 0
  i, j = max_i, max_j
  while i > 0 and j > 0:
    curr_score = dp[i][j]
    diag_score = dp[i - 1][j - 1]
    up_score = dp[i][j - 1]
    left_score = dp[i - 1][j]
    if curr_score == diag_score + (2 if seq1[i - 1] == seq2[j - 1] else -2):
      align1 = seq1[i - 1] + align1
      align2 = seq2[j - 1] + align2
      score += (2 if seq1[i - 1] == seq2[j - 1] else -2)
      i -= 1
      j -= 1
    elif curr_score == left_score - 2:
      align1 = seq1[i - 1] + align1
      align2 = '-' + align2
      score += -2
      i -= 1
    elif curr_score == up_score - 2:
      align1 = '-' + align1
      align2 = seq2[j - 1] + align2
      score += -2
      j -= 1
    else:
      break
  result(align1, align2, score)
  return None

seq_1=st.text_input("Enter Sequence 1")
seq_2=st.text_input("Enter Sequence 2")
st.button("Submit")
needleman_wunsch(seq_1, seq_2)
smith_waterman(seq_1, seq_2)
