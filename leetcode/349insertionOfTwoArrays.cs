// my solution (Beats 86.24% of users with C#)
public class Solution
{
    public int[] Intersection(int[] nums1, int[] nums2)
    {
        List<int> inter = new List<int>();
        for (int i = 0; i < nums1.Length; i++)
        {
            for (int j = 0; j < nums2.Length; j++)
            {
                if (nums1[i] == nums2[j] && !inter.Contains(nums1[i]))
                {
                    inter.Add(nums1[i]);
                }
            }
        }
        return inter.ToArray();
    }
}
// other solutions (beats 99%)
public class Solution
{
    public int[] Intersection(int[] nums1, int[] nums2)
    {
        return GetAll(nums1, nums2).ToArray();
    }
    public IEnumerable<int> GetAll(int[] nums1, int[] nums2)
    {
        var set = new HashSet<int>(nums2);
        for (int i = 0; i < nums1.Length; i++)
        {
            if (set.Remove(nums1[i]))
            {
                yield return nums1[i];
            }
        }
    }
}