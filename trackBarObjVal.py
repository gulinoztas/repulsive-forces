
TrackBarObjVal = 2478127
TrackBarDeviation = 234234
valTrackBarObjVal = TrackBarObjVal * 0.10
TrackBarDeviation = TrackBarDeviation if TrackBarDeviation + TrackBarObjVal <= 10 else 10 - TrackBarObjVal
valTrackBarDeviation = TrackBarDeviation*0.10
TrackBarSatisfaction = 10-(TrackBarObjVal-TrackBarDeviation)
valTrackBarSatisfaction = TrackBarSatisfaction * 0.10
