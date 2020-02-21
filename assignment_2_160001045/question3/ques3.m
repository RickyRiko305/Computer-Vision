a = load('..\question2\sameScore.txt');
b = load('..\question2\differentScore.txt');
for k=1:9
    accuracyPlots(a(:,k),b(:,k),1)
end