from PIL import Image
import av, os, math, operator

comparsion_threshold = 2000
last_index = 0

def main():

	for file_name in os.listdir('video/'):
		if not file_name.startswith('.'):
			handle_video(file_name)

def handle_video(video_name):
	global last_index
	last_index = 0

	container = av.open('video/' + video_name)
	video = next(s for s in container.streams if s.type == b'video')

	name_wo_ext = video_name.split('.')[0]

	for packet in container.demux(video):
		for frame in packet.decode():
				frame.to_image().save('img/' + name_wo_ext  + '-' + str(frame.index) + '.jpg')
				if frame.index > 0:
					if are_same_images('img/' + name_wo_ext + '-' + str(frame.index) + '.jpg', 'img/' + name_wo_ext + '-' + str(last_index) + '.jpg'):
						os.remove('img/' + name_wo_ext + '-' + str(frame.index) + '.jpg')
						print ('same!' + str(frame.index))
					else:
						last_index = frame.index

def are_same_images(path0, path1):
	h0 = Image.open(path0).histogram()
	h1 = Image.open(path1).histogram()

	rms = math.sqrt(reduce(operator.add, map(lambda a,b: (a-b)**2, h0, h1))/len(h0))
	return rms < comparsion_threshold

main()
