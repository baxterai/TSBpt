import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4])
y1 = np.array([0.0, 0.42544126510620117, 0.4689004719257355, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan])
y2 = np.array([0.0, 0.5252946615219116, 0.5836884379386902, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan])
y3 = np.array([0.0, 0.49481841921806335, 0.539782702922821, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan])
y4 = np.array([0.0, 0.5054967999458313, 0.5646486878395081, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan])
y5 = np.array([0.0, 0.4526788890361786, 0.5098543167114258, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan])

'''
y1 = np.array([0.0, 0.4715276062488556, 0.504429817199707, 0.5217463970184326, 0.5327208638191223, 0.540026068687439, 0.5456399321556091, 0.5492268204689026, 0.5532917976379395])
y2 = np.array([0.0, 0.5848015546798706, 0.6353920698165894, 0.6581273078918457, 0.6719351410865784, 0.6809597015380859, 0.6881480813026428, 0.6926000118255615, 0.6963947415351868])
y3 = np.array([0.0, 0.5370364785194397, 0.5751139521598816, 0.5930986404418945, 0.6051175594329834, 0.6125524044036865, 0.6182177066802979, 0.6243066191673279, 0.6271749138832092])
y4 = np.array([0.0, 0.5731309652328491, 0.6191977262496948, 0.6443995237350464, 0.6583037972450256, 0.668066680431366, 0.6770032048225403, 0.681004524230957, 0.6841686367988586])
y5 = np.array([0.0, 0.5113475322723389, 0.556266188621521, 0.5777371525764465, 0.5915654301643372, 0.6009089350700378, 0.6087168455123901, 0.612263023853302, 0.615630567073822])
'''

l1, = plt.plot(x, y1, color='green', label='lay=1, hid=768, head=12 (176MB)')
l2, = plt.plot(x, y2, color='blue', label='lay=12, hid=768, head=12 (486MB)')
l3, = plt.plot(x, y3, color='red', label='lay=1r12, hid=768, head=12 (176MB)')
l4, = plt.plot(x, y4, color='pink', label='lay=1r12, hid=1792, head=28 (norm:496MB)')
l5, = plt.plot(x, y5, color='lightgreen', label='lay=1, hid=768, head=24 (norm:407MB)')

plt.xticks(np.arange(min(x), max(x)+0.5, 0.5))
plt.yticks(np.arange(0, 0.7+0.1, 0.1))

plt.xlabel("number of codeparrot-ds train samples (x1280000)")
plt.ylabel("Causal LM test accuracy (Top-1)")
plt.title("GPT2 Recursive Transformer")

plt.legend(handles=[l2, l3, l4, l1, l5])

plt.show()
