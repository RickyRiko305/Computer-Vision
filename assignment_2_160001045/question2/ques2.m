test_files = dir('test_images');
train_files = dir('ML');
fileID1 = fopen('sameScore.txt','w');
fileID2 = fopen('differentScore.txt','w');
for i=3:length(test_files)
    for j=3:length(train_files)
        testFileName=test_files(i).name;
        trainFileName=train_files(j).name;
        testFileNamePath=strcat('test_images\',testFileName);
        trainFileNamePath=strcat('ML\',trainFileName);
        if i==3
            for k=1:9
                fprintf(fileID1,'%d ',toMatchTestTrain(testFileNamePath,trainFileNamePath,k));
            end
            fprintf(fileID1,'\n')
        else
            for k=1:9
                fprintf(fileID2,'%d ',toMatchTestTrain(testFileNamePath,trainFileNamePath,k));
            end
            fprintf(fileID2,'\n')
        end
    end
end


train_files = dir('PL');
for i=3:length(test_files)
    for j=3:length(train_files)
        testFileName=test_files(i).name;
        trainFileName=train_files(j).name;
        testFileNamePath=strcat('test_images\',testFileName);
        trainFileNamePath=strcat('PL\',trainFileName);
        if i==4
            for k=1:9
                fprintf(fileID1,'%d ',toMatchTestTrain(testFileNamePath,trainFileNamePath,k));
            end
            fprintf(fileID1,'\n')
        else
            for k=1:9
                fprintf(fileID2,'%d ',toMatchTestTrain(testFileNamePath,trainFileNamePath,k));
            end
            fprintf(fileID2,'\n')
        end
    end
end


train_files = dir('WL');
for i=3:length(test_files)
    for j=3:length(train_files)
        testFileName=test_files(i).name;
        trainFileName=train_files(j).name;
        testFileNamePath=strcat('test_images\',testFileName);
        trainFileNamePath=strcat('WL\',trainFileName);
        if i==5
            for k=1:9
                fprintf(fileID1,'%d ',toMatchTestTrain(testFileNamePath,trainFileNamePath,k));
            end
            fprintf(fileID1,'\n')
        else
            for k=1:9
                fprintf(fileID2,'%d ',toMatchTestTrain(testFileNamePath,trainFileNamePath,k));
            end
            fprintf(fileID2,'\n')
        end
    end
end


train_files = dir('MB');
for i=3:length(test_files)
    for j=3:length(train_files)
        testFileName=test_files(i).name;
        trainFileName=train_files(j).name;
        testFileNamePath=strcat('test_images\',testFileName);
        trainFileNamePath=strcat('MB\',trainFileName);
        if i==6
            for k=1:9
                fprintf(fileID1,'%d ',toMatchTestTrain(testFileNamePath,trainFileNamePath,k));
            end
            fprintf(fileID1,'\n')
        else
            for k=1:9
                fprintf(fileID2,'%d ',toMatchTestTrain(testFileNamePath,trainFileNamePath,k));
            end
            fprintf(fileID2,'\n')
        end
    end
end
