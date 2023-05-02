func arraySign(nums []int) int {
    answer:=0
    for _,v:=range nums{
        if v==0{
            return 0
        }
        if v<0{
            answer++
        }
    }
    if answer%2==0{
        return 1
    }
    return -1
}