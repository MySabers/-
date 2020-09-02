/**
 * 选择排序的实现
 */
public class SelectionSort{
    public int[] sort(int[] array){
        for (int i = 0; i < array.length; i++){
            int minNum = array[i];
            int minIndex = i;
            for (int j = i; j < array.length; j++){
                if (minNum > array[j]){
                    minNum = array[j];
                    minIndex = j;
                }
            }
            array[minIndex] = array[i];
            array[i] = minNum;
        }
        return array;
    }

    public static void main(String[] args) {
        SelectionSort selectionSort = new SelectionSort();
        int[] array = new int[]{7,2,34,9,-1,7};
        int[] sortArray = selectionSort.sort(array);
        for (int num : sortArray){
            System.out.print(num + ", ");
        }
        
    }
}