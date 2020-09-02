/**
 * bubble sort java realize
 * 冒泡排序的实现
 */
public class BubbleSort{
    
    /**
     * 冒泡排序从小到大
     */
    public int[] bubbleSortFromSmallToLarge(int[] array){
        for (int i = 0; i < array.length; i++){
            boolean flag = false;
            for (int j = 0; j < array.length - i - 1; j++){
                if (array[j] > array[j + 1]){
                    int temp = array[j];
                    array[j + 1] = array[j];
                    array[j] = temp;
                    flag = true;
                }
            }
            if (!flag) {  break; }
        }
        return array;
    }

    /**
     * 冒泡排序从大到小
     */
    public int[] bubbleSortFromLargeToSmall(int[] array){
        for (int i = 0; i < array.length; i++){
            boolean flag = false;
            for (int j = array.length - 1; j > i; j--){
                if (array[j] > array[j - 1]){
                    int temp = array[j];
                    array[j] = array[j - 1];
                    array[j - 1] = temp;
                    flag = true;
                }
            }
            if (!flag){  break; }
        }
        return array;
    }


    public static void main(String[] args) {
        int[] array = new int[]{1,5,3,6,4,7,9,8};
        BubbleSort bubbleSort = new BubbleSort();
        int[] sortArray = bubbleSort.bubbleSortFromLargeToSmall(array);
        for (int num : sortArray){
            System.out.print(num);
        }
    }    
}