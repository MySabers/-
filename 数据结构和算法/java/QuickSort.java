public class QuickSort{

    public void sort(int[] array, int startIndex, int endIndex){
        if (startIndex >= endIndex){
            return;
        }
        int p = partition(array, startIndex, endIndex);
        sort(array, startIndex, p - 1);
        sort(array, p + 1, endIndex);
    }

    public int partition(int[] array, int startIndex, int endIndex){
        int x = startIndex;
        int y = startIndex;
        for (; x <= endIndex; x++){
            if (array[x] <= array[endIndex]){
                int tmp = array[x];
                array[x] = array[y];
                array[y] = tmp;
                y++;
            }
        }
        return --y;
    }


    public static void main(String[] args) {
        QuickSort quickSort = new QuickSort();
        int[] array = new int[]{1, 2, -1, 8, -7 , 5, 4, 9};
        quickSort.sort(array, 0, array.length - 1);
        for (int s : array){
            System.out.println(s);
        }
    }


}