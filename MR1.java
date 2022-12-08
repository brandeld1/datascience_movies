import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class test {

  public static class TokenizerMapper
       extends Mapper<Object, Text, Text, DoubleWritable>{

    private Text word = new Text();

    public void map(Object key, Text value, Context context
                    ) throws IOException, InterruptedException {
      StringTokenizer itr = new StringTokenizer(value.toString());
      itr.nextToken();
      while(itr.hasMoreTokens()) {
	    	  String data[] = itr.nextToken().toString().split(",");
	    	  if(data.length>=5) {
		          String genresList = data[2]; // get the list of genres
		          String[] genres = genresList.toString().split("\\|"); // split the list of genres
		          DoubleWritable one = new DoubleWritable(1); //create a writable for 1
		          for(int i=0;i<genres.length;i++){
		        	  String yeargenre = data[1]+","+genres[i]; //get the year and genre for each in the list
		        	  word.set(yeargenre); //set the word
		        	  context.write(word, one); //write the word and 1 to context
		          }
	    	  }
	    }
    }
  }

  public static class DoubleSumReducer
       extends Reducer<Text,DoubleWritable,Text,DoubleWritable> {
    private DoubleWritable result = new DoubleWritable();

    public void reduce(Text key, Iterable<DoubleWritable> values,
                       Context context
                       ) throws IOException, InterruptedException {
      double sum = 0;
      for (DoubleWritable val : values) {
        sum += val.get(); //sum up the values(which are all 1)
      }
      result.set(sum); //write the sum to result
      context.write(key, result); //write the key and result to context
    }
  }

  public static void main(String[] args) throws Exception {
    Configuration conf = new Configuration();
    Job job = Job.getInstance(conf, "word count");
    job.setJarByClass(test.class);
    job.setMapperClass(TokenizerMapper.class);
    job.setCombinerClass(DoubleSumReducer.class);
    job.setReducerClass(DoubleSumReducer.class);
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(DoubleWritable.class);
    FileInputFormat.addInputPath(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path(args[1]));
    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }
}