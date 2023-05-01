func average(salary []int) float64 {
    sort.Ints(salary)
    sum:=0
    length:=len(salary)
    for _,v :=range salary[1:length-1]{
        sum+=v
    }
    return float64(sum)/float64(length-2)
    
}