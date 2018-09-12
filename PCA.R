library(MVA)
library(psych)

df <- read.csv("C:/Users/Slayer/Desktop/축구분석/1차 선처리(5경기 데이터).csv")

ccsv <- transform(df,v0=scale(Home),v1=scale(Result),v2=scale(Not_Epl),v3=scale(Home_Play_1),v4=scale(Home_Play_2),v5=scale(Home_Play_Score),
                  v6=scale(Enemy_1),v7=scale(Enemy_2),v8=scale(Enemy_Score),v9=scale(Me_Play_Corner),v10=scale(Me_Play_Shot),
                  v11=scale(Me_Play_Shot_Target),v12=scale(Me_Play_Foul),v13=scale(Me_Play_Offside),v14=scale(You_Play_Corner),v15=scale(You_Play_Shot),
                  v16=scale(You_Play_Shot_Target),v17=scale(You_Play_Foul),v18=scale(You_Play_Offside),v19=scale(Home_Play_Share),v20=scale(Away_Play_Share),
                  v21=scale(Five_Home_Play_1),v22=scale(Five_Home_Play_2),v23=scale(Five_Home_Play_Score),v24=scale(Five_Enemy_1),v25=scale(Five_Enemy_2),
                  v26=scale(Five_Enemy_Score),v27=scale(Five_Me_Play_Corner),v28=scale(Five_Me_Play_Shot),v29=scale(Five_Me_Play_Shot_Target),v30=scale(Five_Me_Play_Foul),
                  v31=scale(Five_Me_Play_Offside),v32=scale(Five_You_Play_Corner),v33=scale(Five_You_Play_Shot),v34=scale(Five_You_Play_Shot_Target),v35=scale(Five_You_Play_Foul),
                  v36=scale(Five_You_Play_Offside),v37=scale(Five_Home_Play_Share),v38=scale(Five_Away_Play_Share),v39=scale(rest_time))

ccsv_2 <- ccsv[,c("Team", "v1","v2","v3","v4","v5","v6","v7","v8","v9","v10","v11","v12","v13","v14","v15","v16","v17","v18","v19","v20",
                  "v21","v22","v23","v24","v25","v26","v27","v28","v29","v30","v31","v32","v33","v34","v35","v36","v37","v38","v39")]

cor(ccsv_2[,-1])

round(cor(ccsv_2[,-1]), digits=3)

plot(ccsv_2[,-1])

secu_prcomp <- prcomp(ccsv_2[,c(2:40)]) # 첫번째 변수 회사명은 빼고 분석 >  > summary(secu_prcomp)

summary(secu_prcomp)
print(secu_prcomp)

plot(prcomp(ccsv_2[,c(2:40)]), type="l", sub = "Scree Plot")

biplot(prcomp(ccsv_2[,c(2:40)]), cex = c(0.7, 0.8))

secu_pc1 <- predict(secu_prcomp)[,1]
secu_pc2 <- predict(secu_prcomp)[,2]
text(secu_pc1, secu_pc2, labels = ccsv_2$result,cex = 0.7, pos = 4, col = "blue")