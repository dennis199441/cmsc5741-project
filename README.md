# Youtube-8M Video-Level Features Analysis
In this project, we will apply various big data analytics techniques and algorithms in order to study the YouTube-8M dataset which contains machine generated labels, RGB features and audio features
for each videos on YouTube platform. We will find out the dominant video categories, frequent itemsets of video categories and group videos into clusters using available features.

## Dataset
YouTube-8M video-level features dataset is used in this project. Video-level features are stored as tensorflow.Example protocol buffers. A tensorflow.Example proto is reproduced here in text format:
```
features: {
  feature: {
    key  : "id"
    value: {
      bytes_list: {
        value: (Video id)
      }
    }
  }
  feature: {
    key  : "labels"
    value: {
      int64_list: {
        value: [1, 522, 11, 172]  # label list
      }
    }
  }
  feature: {
    # Average of all 'rgb' features for the video
    key  : "mean_rgb"
    value: {
      float_list: {
        value: [1024 float features]
      }
    }
  }
  feature: {
    # Average of all 'audio' features for the video
    key  : "mean_audio"
    value: {
      float_list: {
        value: [128 float features]
      }
    }
  }
}
```

## Task
1. Dominant categories on YouTube
2. K-th Frequent Itemsets of video categories
3. Group videos into clusters according to audio features

## Approach
1. Count video categories under MapReduce framework using key = category id
2. Implement Apriori algorithm under MapReduce framework
3. Implement K-Means algorithm
