/**
 * 插入排序的实现
 */
public class InsertionSort{

    public int[] sort(int[] array){
        for (int i = 1; i < array.length; i++){
            int value = array[i];
            int j = i - 1;
            for (; j >= 0; --j){
                if (array[j] > value){
                    array[j + 1] = array[j];
                }
                else{
                    break;
                }
            }
            array[j + 1] = value;
        }
        return array;
    }
    

    public static void main(String[] args) {
        InsertionSort InsertionSort = new InsertionSort();
        int[] array = new int[]{3, 7, 4, 3, -1, 2, 9, 4, 0};
        int[] sortArray = InsertionSort.sort(array);
        for (int a : sortArray){
            System.out.print(a + ", ");
        }
    }

}