import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from scipy.ndimage import label
from scipy.stats import zscore


import warnings


def timedomain(rr):
    results = {}

    hr = 60000/rr
    return {"data" : np.sqrt(np.mean(np.square(np.diff(rr))))}


def detect_peaks(ecg_signal, threshold=0.3, qrs_filter=None):
    if qrs_filter is None:
        t = np.linspace(1.5 * np.pi, 3.5 * np.pi, 15)
        qrs_filter = np.sin(t)
    

    ecg_signal = (ecg_signal - ecg_signal.mean()) / ecg_signal.std()

    similarity = np.correlate(ecg_signal, qrs_filter, mode="same")
    similarity = similarity / np.max(similarity)

    return ecg_signal[similarity > threshold].index, similarity


def get_plot_ranges(start=10, end=20, n=5):

    distance = end - start
    for i in np.arange(start, end, np.floor(distance/n)):
        yield (int(i), int(np.minimum(end, np.floor(distance/n) + i)))


def group_peaks(p, threshold=5):
    output = np.empty(0)
    peak_groups, num_groups = label(np.diff(p) < threshold)
    for i in np.unique(peak_groups)[1:]:
        peak_group = p[np.where(peak_groups == i)]
        output = np.append(output, np.median(peak_group))
    return output

def getRmssd(data):
    print(data)
    df = pd.DataFrame(data, columns =['ms', 'heartrate']) 
    sampfrom = 60000
    sampto = 70000
    nr_plots = 1

    for start, stop in get_plot_ranges(sampfrom, sampto, nr_plots):

        cond_slice = (df.index >= start) & (df.index < stop) 
        ecg_slice = df.heartrate[cond_slice]


        peaks, similarity = detect_peaks(ecg_slice, threshold=0.3)
        
        plt.figure(figsize=(20, 15))
    peaks, similarity = detect_peaks(df.heartrate, threshold=0.3)


    grouped_peaks = group_peaks(peaks)

    peaks, similarity = detect_peaks(df.heartrate, threshold=0.3)


    grouped_peaks = group_peaks(peaks)

    rr = np.diff(grouped_peaks)


    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        sns.kdeplot(rr, label="rr-intervals", color="#A651D8", shade=True)

    outlier_low = np.mean(rr) - 2 * np.std(rr)
    outlier_high = np.mean(rr) + 2 * np.std(rr)


    rr_corrected = rr.copy()
    rr_corrected[np.abs(zscore(rr)) > 2] = np.median(rr)

    sampfrom = 240000
    sampto = 250000
    nr_plots = 1

    peaks, similarity = detect_peaks(df.heartrate, threshold=0.3)

    grouped_peaks = group_peaks(peaks)

    rr = np.diff(grouped_peaks)


    return timedomain(rr*2)
    
    
