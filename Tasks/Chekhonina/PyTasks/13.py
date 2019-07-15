h_1, m_1, s_1, h_2, m_2, s_2 = map(int, input().split())
print(s_2 - s_1 + (m_2 - m_1) * 60 + (h_2 - h_1) * 3600)
