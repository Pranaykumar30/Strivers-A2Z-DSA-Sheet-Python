#https://www.codingninjas.com/studio/problems/team-contest_6840309?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def countTeamHelper(a, start, mid, end, count):
    leftIndex, rightIndex = start, mid + 1
    temp = [0] * (end - start + 1)
    tempIndex = 0

    while leftIndex <= mid and rightIndex <= end:
        if a[leftIndex] <= a[rightIndex]:
            temp[tempIndex] = a[leftIndex]
            tempIndex += 1
            leftIndex += 1
        else:
            index = next((i for i, x in enumerate(a[leftIndex:mid + 1]) if x > 2 * a[rightIndex]), mid - leftIndex + 1)
            count[0] += mid - (leftIndex + index) + 1
            temp[tempIndex] = a[rightIndex]
            tempIndex += 1
            rightIndex += 1

    while leftIndex <= mid:
        temp[tempIndex] = a[leftIndex]
        tempIndex += 1
        leftIndex += 1
    while rightIndex <= end:
        temp[tempIndex] = a[rightIndex]
        tempIndex += 1
        rightIndex += 1

    tempIndex = 0
    for i in range(start, end + 1):
        a[i] = temp[tempIndex]
        tempIndex += 1

def countTeam(a, start, end, count):
    if start >= end:
        return

    mid = start + (end - start) // 2

    countTeam(a, start, mid, count)
    countTeam(a, mid + 1, end, count)
    countTeamHelper(a, start, mid, end, count)
    return
def team(skill: [int], n: int) -> int:
    count = [0]
    countTeam(skill, 0, n - 1, count)

    return count[0]
