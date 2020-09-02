public class MergeSort{


    public void sort(int[] array,int start ,int end){
        if (start >= end){
            return;
        }
        int middle = (start + end)/2;
        // 拆分
        sort(array, start, middle);
        sort(array, middle + 1, end);
        // 合并
        int[] tmp = new int[end - start + 1];
        int s = start;
        int m = middle + 1;
        int t = 0;
        while(s <= middle && m <= end) {
            if (array[s] >= array[m]){
                tmp[t++] = array[s++];
            } else {
                tmp[t++] = array[m++];
            }
        }
        int x = s;
        int y = middle;
        if (m <= end){
            x = m;
            y = end;
        }
        while (x <= y){
            tmp[t++] = array[x++];
        }
        for (int i = 0; i < tmp.length; i++){
            array[start++] = tmp[i];
        }
    }

    public static void main(String[] args) {
        int[] array = {1, 3, 8, 6, 4, 2, -1, 8};
        MergeSort mergesort = new MergeSort();
        mergesort.sort(array, 0, array.length - 1);
        for (int num : array){
            System.out.println(num);
        }
    }

}